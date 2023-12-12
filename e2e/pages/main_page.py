from fixture.browser import driver
from pages.locators import MainPage, Map
import time
from selenium.webdriver import Keys


def add_obj(name, period, link, info):
    driver.find_element(*MainPage.ADD_BUTTON).click()
    time.sleep(1)
    driver.find_element(*MainPage.NAME_OBJ).click()
    driver.find_element(*MainPage.NAME_OBJ).send_keys(name)
    driver.find_element(*MainPage.PERIOD).send_keys(period)
    driver.find_element(*MainPage.MAP_LINK).send_keys(link)
    driver.find_element(*MainPage.COMMENT).send_keys(info)
    driver.find_element(*MainPage.ADD_BUTTON_OBJ).click()


def add_in_favorites():
    driver.find_element(*MainPage.FAVOURITES).click()
    time.sleep(2)
    s = driver.find_element(*MainPage.FAVOURITES).get_attribute('title')
    assert s == "Открепить", "Закрепить в избранном не удалось"


def start_active_monitoring():
    driver.find_element(*MainPage.INTENSIVE_MONITORING).click()
    time.sleep(1)
    s = driver.find_element(*MainPage.INTENSIVE_MONITORING).get_attribute('title')
    assert s == "Вернуть обычное наблюдение", "Режим активного наблюдения не включен"


def stop_collection_data():
    driver.find_element(*MainPage.STOP_COLLECTING_DATA).click()
    time.sleep(1)
    driver.find_element(*MainPage.ADD_BUTTON_OBJ).click()
    s = driver.find_element(*MainPage.STOP_COLLECTING_DATA).get_attribute("title")
    assert s == "Запустить", "Стоп не произошел"


def start_collection_data():
    driver.find_element(*MainPage.STOP_COLLECTING_DATA).click()
    time.sleep(1)
    driver.find_element(*MainPage.ADD_BUTTON_OBJ).click()
    s = driver.find_element(*MainPage.STOP_COLLECTING_DATA).get_attribute("title")
    assert s == "Приостановить", "Запуск не произошел"


# Тут буду сохранять значение атрибута "value"
def edit_obj():
    driver.find_element(*MainPage.EDIT).click()
    time.sleep(1)
    driver.find_element(*MainPage.NAME_OBJ).click()
    s1 = driver.find_element(*MainPage.NAME_OBJ)
    s2 = driver.find_element(*MainPage.PERIOD)
    s3 = driver.find_element(*MainPage.COMMENT)
    s1.send_keys(Keys.BACKSPACE)
    s2.send_keys(Keys.BACKSPACE)
    s3.send_keys(Keys.BACKSPACE)
    driver.find_element(*MainPage.ADD_BUTTON_OBJ).click()


def check_edit_obg():
    driver.find_element(*MainPage.EDIT).click()
    s1 = driver.find_element(*MainPage.CHECK_NAME).get_attribute('value')
    s2 = driver.find_element(*MainPage.CHECK_PERIOD).get_attribute('value')
    s3 = driver.find_element(*MainPage.CHECK_COMMENT).get_attribute('value')
    assert s1 == 'AUTOTES', 'Редактирование поля не удалось'
    assert s2 == '1', 'Редактирование поля не удалось'
    assert s3 == 'АВТОТЕС', 'Редактирование поля не удалось'
    driver.find_element(*MainPage.ADD_BUTTON_OBJ).click()


def delete_obj():
    time.sleep(1)
    driver.find_element(*MainPage.DELETE_BTN).click()
    time.sleep(2)
    driver.find_element(*MainPage.ADD_BUTTON_OBJ).click()


def add_obj_map(name, period):
    driver.find_element(*Map.TAB_MAP).click()
    time.sleep(1)
    driver.find_element(*Map.MAP).click()
    time.sleep(1)
    driver.find_element(*MainPage.NAME_OBJ).send_keys(name)
    driver.find_element(*MainPage.PERIOD).send_keys(period)
    driver.find_element(*MainPage.ADD_BUTTON_OBJ).click()


def check_added_obj_map(name, period):
    driver.find_element(*MainPage.TAB_TITLE).click()
    time.sleep(1)
    driver.find_element(*MainPage.EDIT).click()
    time.sleep(1)
    s1 = driver.find_element(*MainPage.CHECK_NAME).get_attribute('value')
    s2 = driver.find_element(*MainPage.CHECK_PERIOD).get_attribute('value')
    assert s1 == name, 'Добавление объекта поля не удалось'
    assert s2 == period, 'Добавление объекта поля не удалось'
    driver.find_element(*MainPage.CLOSE_MODAL_WINDOW).click()