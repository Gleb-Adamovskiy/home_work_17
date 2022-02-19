import json

def load_candidates_from_json():
    """
    загрузка всех кандидатов из файла в список
    """
    with open("candidates.json", encoding="utf8") as f:
        candidates = json.load(f)
    return candidates


def get_candidate(candidate_id):
    """
    возвращаем кандидата по id
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_skill(skill_name):
    """
    возвращает список кандидатов по параметру skills
    """
    candidates = load_candidates_from_json()
    skills_candidates = []
    skill_name_lower = skill_name.lower()

    for candidate in candidates:
        if skill_name_lower in candidate["skills"].lower().split(", "):
            skills_candidates.append(candidate)

    return skills_candidates


def build_page(candidates):
    """
    формирует страницу представления
    """
    page = ""
    for candidate in candidates:
        page += candidate["name"] + "\n"
        page += candidate["position"] + "\n"
        page += candidate["skills"] + "\n"
        page += "\n"

    return "<pre>" + page + "</pre>"
