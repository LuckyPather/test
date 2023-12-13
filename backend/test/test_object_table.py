from methods import generators
from methods import object_table

"""Работа с БД"""


# Создаю таблицу с 10 пользователями, проверяю.
def test_create_10_obj():
    object_table.add_objects(10)
    object_table.check_count(10, "objects")


# Очищаю таблицу, проверяю что она очистилась.
def test_delete_data():
    object_table.delete_data("objects")
    object_table.check_count(0, "objects")


"""Работа через API библиотека request"""


# Добавляю объект, через апи, библиотека request
def test_request():
    object_table.add_object()
