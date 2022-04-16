import sqlite3
from flask import Flask
import json

def get_data_from_db(sql):
    # подключение к базе данных
    with sqlite3.connect("netflix.db") as connect:
        connect.row_factory = sqlite3.Row
        result = connect.execute(sql).fetchall()
    return result

def search_by_title(title):
    # поиск фильма по названию и сортировка по году релиза
    for i in get_data_from_db(sql=f'''
    SELECT title, release_year, description, country
    FROM netflix
    WHERE title = '{title}'
    ORDER by release_year
    LIMIT 1
    '''):
        return dict(i)

def value_by_years(year_1, year_2):
    # поиск фильмов выпущенных в период между годами
    response = get_data_from_db(sql=f'''
    SELECT title, release_year
    FROM netflix
    WHERE release_year BETWEEN '{year_1}' and '{year_2}'
    LIMIT 100
    ''')
    list_of_films = []
    for i in response:
        list_of_films.append(dict(i))

    return list_of_films

def value_by_reiting(rating):
    # сортировка фильмов по рейтингу
    rait = ''
    if rating == 'children':
        rait = 'rating = "G"'
    elif rating == 'family':
        rait = 'rating = "G" or rating = "PG" or rating = "PG-13"'
    elif rating == 'adult':
        rait = 'rating = "R" or rating = "NC-17"'

    response = get_data_from_db(sql=f'''
    SELECT title, rating, description
    FROM netflix
    WHERE {rait}
    LIMIT 100
    ''')

    list_of_films = []
    for i in response:
        list_of_films.append(dict(i))

    return list_of_films

def search_by_genre(genre):
    # поиск фильмов по жанру
    response = get_data_from_db(sql=f'''
    SELECT title, release_year, description, country, listed_in
    FROM netflix
    WHERE listed_in LIKE '%{genre}%'
    ORDER by release_year DESC
    LIMIT 10
    ''')
    list_of_films = []
    for i in response:
        list_of_films.append(dict(i))

    return list_of_films

def search_actor(actor_1, actor_2):
    # поиск актеров игравших больше двух раз с парой в запросе
    response = get_data_from_db(sql=f'''
    SELECT "cast" 
    FROM netflix
    WHERE "cast" LIKE '%{actor_1}%' and "cast" LIKE '%{actor_2}%'   
    ''')
    actors = []
    results = []
    for i in response:
        casting = dict(i).get("cast").split(", ")
        for key in casting:
            actors.append(key)

    both = [actor_1, actor_2]
    actors = set(actors) - set(both)

    for actor in actors:
        k = 0
        for i in response:
            if actor in dict(i).get("cast"):
                k += 1
        if k > 2:
            results.append(actor)

    return results

def search_by_parametres(type_film, year, genre):
    # поиск фильмов по заданным параметрам
    response = get_data_from_db(sql=f'''
    SELECT "title", "release_year", "description", "type"
    FROM netflix
    WHERE "type" LIKE '%{type_film}%'
    AND "release_year" LIKE '%{year}%'
    AND "listed_in" LIKE '%{genre}%'
    ''')
    list_of_films = []
    for i in response:
        list_of_films.append(dict(i))

    return json.dumps(list_of_films)

app = Flask(__name__)

@app.get('/movie/<title>')
# представление по названию фильма
def view_search_title(title):
    response = search_by_title(title=title)
    return app.response_class(response=json.dumps(response))

@app.get('/movie/<year_1>/to/<year_2>')
# представление фильмов выпущенных в период между годами
def view_search_by_years(year_1, year_2):
    response = value_by_years(year_1=year_1, year_2=year_2)
    return app.response_class(response=json.dumps(response))

@app.get('/rating/<rating>')
# представление фильмов с соответствующим рейтингом
def view_by_reiting(rating):
    response = value_by_reiting(rating=rating)
    return app.response_class(response=json.dumps(response))

@app.get('/genre/<genre>')
# представление фильмов по жанру
def view_by_genre(genre):
    response = search_by_genre(genre=genre)
    return app.response_class(response=json.dumps(response))

if __name__ == "__main__":
    app.run()
