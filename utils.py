# Импортируем модуль JSON для работы с этим форматом
import json

# Импортируем рендер шаблона для создания страничек кандидатов
from flask import render_template


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
    for i in load_candidates("candidates.json"):
        if i["pk"] == id:
            return render_template("card.html", _dict=i)


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


def get_by_name(name):
    """
    :param name: Имя для поиска
    :return: Преформатированную строку кандидатов с данным именем
    """
    list_of_candidates_for_output = []
    for i in load_candidates("candidates.json"):
        list_of_full_name = i["name"].split(" ")
        if name.lower() == list_of_full_name[0].lower():
            list_of_candidates_for_output.append("Имя кандидата - " + i["name"])
            list_of_candidates_for_output.append("Позиция кандидата - " + i["position"])
            list_of_candidates_for_output.append("Навыки кандидата -  " + i["skills"] + "\n\n")
    string_of_candidates_for_output = "\n".join(list_of_candidates_for_output)
    return f"<pre>{string_of_candidates_for_output}</pre>"
