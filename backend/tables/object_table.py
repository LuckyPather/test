from config import connect1, connect2
from tables.generators import data_generator
from sqlalchemy import text
from config import login, delete_data

# В зависимости от точки запуска теста, нужно проверять импортированные пути, к примеру
# если запустить данную функцию из другой папки, то она не будет знать о модуле generators, поэтому
# до generators прописывается полный путь

"""Работа напрямую с БД"""


# Добавляет объекты в таблицу objects
def add_objects(count):
    sql_add_obj = 'INSERT INTO objects(name, latitude, longitude, comment, period, "isFavorite", enabled, ' \
                  '"createdAt", "updatedAt") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    connect1().executemany(sql_add_obj, data_generator(count))


# Проверяем, что количество записей равняется count из метода add_object
def check_count(count, name):
    # Получаем объект в виде класса
    sql_check_count = connect2().execute(text(f"SELECT COUNT(*) FROM {name};"))
    for row in sql_check_count:
        # Обращаемся к 1 элементу массива, чтобы получить кол-во строк в таблице
        extracted_row = row[0]
        assert extracted_row == count, "Количество строк в таблице object, отличается от ожидаемого"


# Удаляет данные из таблицы
def delete_data(name):
    connect1().execute(f"DELETE FROM {name}")


"""Работа с АПИ используя Request"""


# Добавление объекта, используя request
def add_object():
    url = 'https://localhost/objects'
    data = \
        {
            "name": "test2",
            "latitude": "60",
            "longitude": "50",
            "comment": "test",
            "link": "<string>",
            "period": 3600,
            "isFavorite": False,
            "enabled": True
        }
    # Вызываем функцию логин, которая возвращает сессию с куками, после чего передаем туда url и json data
    responce = login().post(url, json=data, verify=False)
    print("Статус код:", responce.status_code)
    print("Ответ сервера", responce.text)
