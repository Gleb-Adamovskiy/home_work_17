from flask import Flask
import utils as u

app = Flask(__name__)

# стартовая страница с выводом всех кандидатов
@app.route('/',)
def page_index():
    candidates = u.load_candidates_from_json()
    page = u.build_page(candidates)
    return page

# страница кандидатов с конкретными навыками
@app.route('/skill/<skill_name>',)
def page_skill_candidate(skill_name):
    candidate = u.get_candidates_by_skill(skill_name)
    page = u.build_page(candidate)
    return page

# страница кандидата по id
@app.route('/candidate/<int:candidate_id>',)
def page_candidate(candidate_id):
    candidate = u.get_candidate(candidate_id)
    candidates = [candidate]
    candidate_image = u.candidate_image(candidate_id)
    page = u.build_page(candidates)
    return f"{candidate_image} {page}"

app.run()
