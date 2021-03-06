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
    :return: Заполненный шаблон имен всех кандидатов
    """
    return render_template("list.html", list=load_candidates("candidates.json"))


def get_by_pk(id):
    """
    :param id: Идентификатор (номер) кандидата
    :return: Заполненный шаблон кандидата по его номеру
    """
    for i in load_candidates("candidates.json"):
        if i["pk"] == id:
            return render_template("card.html", _dict=i)


def get_by_skill(skill):
    """
    :param skill: Навык для поиска
    :return: Заполненный шаблон всех кандидатов с данным скиллом
    """
    list_of_candidates_for_output = []
    for i in load_candidates("candidates.json"):
        list_of_skills = i["skills"].split(", ")
        for k in list_of_skills:
            if skill.lower() == k.lower():
                list_of_candidates_for_output.append(i)
                break
    return render_template("skill.html", list=list_of_candidates_for_output,
                           skill=skill.title(), _len=len(list_of_candidates_for_output))


def get_by_name(name):
    """
    :param name: Имя для поиска
    :return: Заполненный шаблон всех кандидатов с данным именем
    """
    list_of_candidates_for_output = []
    for i in load_candidates("candidates.json"):
        list_of_full_name = i["name"].split(" ")
        if name.lower() == list_of_full_name[0].lower():
            list_of_candidates_for_output.append(i)
    return render_template("search.html", list=list_of_candidates_for_output,
                           name=name.title(), _len=len(list_of_candidates_for_output))
