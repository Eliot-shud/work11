#импорт json
import json

#возвращает список всех кандидатов
def load_candidates_from_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8')as file:
        return json.load(file)

#возвращает одного кандидата по его id
def get_candidate(candidate_id: int) -> dict:
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate

#возвращает кандидатов по имени
def get_candidates_by_name(candidate_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result

#возвращает кандидатов по навыку
def get_candidates_by_skill(skill_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result


print(get_candidates_by_skill('python'))


