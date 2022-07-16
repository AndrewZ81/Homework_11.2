# Импортируем модуль JSON для работы с этим форматом
import json


def load_candidates(file_with_candidates):
    """
    :param file_with_candidates: Файл с кандидатами формата JSON
    :return: Список кандидатов
    """
    with open(file_with_candidates, encoding="utf-8") as file:
        candidates = json.loads(file.read())
    return candidates


def get_all():
    """
    :return: Преформатированную строку кандидатов
    """
    list_of_candidates_for_output = []
    for i in load_candidates("candidates.json"):
        list_of_candidates_for_output.append("Имя кандидата - " + i["name"])
        list_of_candidates_for_output.append("Позиция кандидата - " + i["position"])
        list_of_candidates_for_output.append("Навыки кандидата -  " + i["skills"] + "\n\n")
    string_of_candidates_for_output = "\n".join(list_of_candidates_for_output)
    return f"<pre>{string_of_candidates_for_output}</pre>"


def get_by_pk(id):
    """
    :param id: Идентификатор (номер) кандидата
    :return: Данные кандидата по его номеру
    """
    list_of_candidate_for_output = []
    url = ""
    for i in load_candidates("candidates.json"):
        if i["pk"] == id:
            url = i["picture"]
            list_of_candidate_for_output.append("Имя кандидата - " + i["name"])
            list_of_candidate_for_output.append("Позиция кандидата - " + i["position"])
            list_of_candidate_for_output.append("Навыки кандидата -  " + i["skills"] + "\n\n")
    string_of_candidate_for_output = "\n".join(list_of_candidate_for_output)
    return f"<img src={url}>\n<pre>{string_of_candidate_for_output}</pre>"


def get_by_skill(skill):
    """
    :param skill: Навык для поиска
    :return: Преформатированную строку кандидатов с данным навыком
    """
    list_of_candidates_for_output = []
    for i in load_candidates("candidates.json"):
        list_of_skills = i["skills"].split(", ")
        for k in list_of_skills:
            if skill.lower() == k.lower():
                list_of_candidates_for_output.append("Имя кандидата - " + i["name"])
                list_of_candidates_for_output.append("Позиция кандидата - " + i["position"])
                list_of_candidates_for_output.append("Навыки кандидата -  " + i["skills"] + "\n\n")
                break
    string_of_candidates_for_output = "\n".join(list_of_candidates_for_output)
    return f"<pre>{string_of_candidates_for_output}</pre>"
