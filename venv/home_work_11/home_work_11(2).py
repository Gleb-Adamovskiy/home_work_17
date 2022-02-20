from flask import Flask, render_template
import utils as u

app = Flask(__name__)
# стартовая страница со списком всех кандидатов
@app.route('/',)
def page_candidates():
    candidates = u.load_candidates_from_json()
    return render_template("index.html", candidates=candidates)

# страница конкретного кандидата
@app.route('/candidate/<int:candidate_id>',)
def page_candidate_by_id(candidate_id):
    candidate = u.get_candidate(candidate_id)
    return render_template("card.html", candidate=candidate)

# страница поиска кандидата по имени
@app.route('/search/<candidate_name>',)
def page_candidate_search(candidate_name):
    candidates = u.get_candidate_name(candidate_name)
    count = len(candidates)
    return render_template("search.html", candidates=candidates, count=count)

# страница поиска кандидата по навыку
@app.route('/skill/<skill_name>',)
def page_candidate_skill(skill_name):
    candidates = u.get_candidates_by_skill(skill_name)
    count = len(candidates)
    return render_template("search.html", candidates=candidates, count=count)

app.run()
