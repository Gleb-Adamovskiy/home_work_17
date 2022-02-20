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


def get_candidate_name(candidate_name):
    """
    возвращаем список кандидатов по имени
    """
    candidates = load_candidates_from_json()
    candidates_name = []
    candidate_name_lower = candidate_name.lower()
    for candidate in candidates:
        if candidate_name_lower in candidate["name"].lower():
            candidates_name.append(candidate)

    return candidates_name


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
