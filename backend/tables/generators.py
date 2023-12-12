from faker import Faker
import random
import string
from datetime import datetime
import pytz


# Основные функции, которые используется перед тестами или после

# Генератор значений для таблицы objects

def data_generator(size):
    data_array = []
    fake = Faker("ru_RU")
    for i in range(size):
        name = fake.city()
        latitude = random.randint(-90, 90)
        longitude = random.randint(-180, 180)
        comment = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        period = random.randint(3600, 4200)
        favorite = random.choice([True, False])
        enabled = random.choice([True, False])
        created = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S %z')
        updated = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S %z')

        # Добавление параметров в массив данных
        data_array.append((name, latitude, longitude, comment, period, favorite, enabled, created, updated))
    return data_array
