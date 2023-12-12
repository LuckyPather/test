from pages import login_page
from fixture.browser import link_, login_
import time


# Проверка наличия элементов
def test_element_is_present():
    link_("http://localhost:8080/")
    time.sleep(3)
    login_page.check_elements()


# Проверка входа с не правильными / правильными данными
def test_login():
    login_page.check_wrong_login()
    time.sleep(10)
    login_("admin", "12345678")
    time.sleep(5)
