from selenium.webdriver import Keys
from fixture.browser import driver, login_
from pages.locators import LoginPage
from fixture import aplication
import time


def check_elements():
    logo = driver.find_element(*LoginPage.LOGO).text
    assert logo == "Авторизация", "Логотип отсутствует или переход на страницу не произошел"
    assert aplication.is_element_present(*LoginPage.LOGIN_INPUT), "Поле ввода логина отсутствует"
    assert aplication.is_element_present(*LoginPage.PASSWORD_INPUT), "Поле ввода пароля отсутствует"
    assert aplication.is_element_present(*LoginPage.LOGIN_BTN), "Кнопка входа отсутствует"


# Если функция Clear не работает, можно использовать метод send_keysFrom, с библиотекой Keys
def check_wrong_login():
    login_("wrong", "test")
    time.sleep(2)
    assert aplication.is_element_present(*LoginPage.ERROR_MESSAGE), "Сообщение об ошибке не получено"
    time.sleep(1)
    driver.find_element(*LoginPage.LOGIN_INPUT).send_keys(Keys.CONTROL + "a")
    driver.find_element(*LoginPage.LOGIN_INPUT).send_keys(Keys.BACK_SPACE)
    time.sleep(1)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(Keys.CONTROL + "a")
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(Keys.BACK_SPACE)
