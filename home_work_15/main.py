import sqlite3
from os.path import join, isfile

DATABASE_PATH = 'animal.db'
SQL_DIR_PATH = 'sql'
INIT_MIGRATION_FILE_PATH = 'init.sql'

def get_sql_from_file(filename):
    content = ''
    if isfile(filename):
        with open(filename) as file:
            content = file.read()
    return content

def main():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    sql = get_sql_from_file(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH))
    cursor.executescript(sql)
    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()




















