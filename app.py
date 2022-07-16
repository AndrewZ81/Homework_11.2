# Импортируем модуль utils для работы с форматом JSON
import utils

# Импортируем класс Flask
from flask import Flask

# Создаём экземпляр Flask
app = Flask(__name__)

# Создаём корневой маршрут
app.add_url_rule("/", view_func=utils.get_all)

# Создаём маршрут для выборки кандидата
app.add_url_rule("/candidates/<int:id>", view_func=utils.get_by_pk)

# Создаём маршрут для поиска кандидатов по навыку
app.add_url_rule("/skills/<skill>", view_func=utils.get_by_skill)

# Запускаем сервер
if __name__ == "__main__":
    app.run()
