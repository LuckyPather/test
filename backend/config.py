import shutil
import psycopg2
from sqlalchemy import create_engine, text
import requests

"""Прямое подключение к бд, через библиотеку psycopg2 и sqlalchemy"""


# Подключение к БД и возвращение объекта cursor для выполнения SQL запросов
def connect1():
    connection = psycopg2.connect(host="127.0.0.1",
                                  user="postgres",
                                  password="13471347",
                                  database="production")
    connection.autocommit = True
    return connection.cursor()


def connect2():
    engine = create_engine("postgresql://postgres:13471347@127.0.0.1:5432/production")
    connection = engine.connect()
    return connection


"""Подключение через API, используя библиотеку request"""


# Авторизация и получение соединения с куками
def login():
    url = 'https://localhost/rbac/okauth_rbac/auth/_'
    data = \
        {
            "login": "admin", "password": "12345678"
        }
    responce = requests.post(url, json=data, verify=False)

    assert responce.status_code == 200, "Ошибка авторизации, проверте доступность домена, и credentials"
    session = requests.Session()
    session.cookies.update(responce.cookies)
    return session


"""Остальные функции, применяемые во всем проекту"""


# Очистка директории
def delete_data(link):
    shutil.rmtree(link)
