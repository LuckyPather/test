from selenium import webdriver
from pages.locators import LoginPage, MainPage
import time
from fixture import aplication

"""Инициализация браузера с параметрами, функции перехода на страницу и логина, драйвер должен быть определен в
переменных среды типа PATH"""

options = webdriver.ChromeOptions()
options.add_argument("--no sandbox")
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)


# Функция отдельного перехода по ссылке
def link_(link):
    driver.get(link)


# Функция отдельного логина
def login_(login, password):
    driver.find_element(*LoginPage.LOGIN_INPUT).send_keys(login)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    time.sleep(3)
    driver.find_element(*LoginPage.LOGIN_BTN).click()


# Функция полного логина
def full_login(link, login, password):
    driver.get(link)
    time.sleep(3)
    driver.find_element(*LoginPage.LOGIN_INPUT).send_keys(login)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    time.sleep(3)
    driver.find_element(*LoginPage.LOGIN_BTN).click()
