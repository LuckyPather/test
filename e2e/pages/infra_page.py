import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fixture.browser import driver
from pages.locators import InfraPageLocators


def go_to_infra_page():
    driver.find_element(*InfraPageLocators.INFRA_PAGE_BTN).click()


def check_servers_are_not_added():
    try:
        time.sleep(1)
        driver.find_element(*InfraPageLocators.INFRA_TABLE_EMPTY).is_displayed()
    except NoSuchElementException:
        print("\nОбнаружены добавленные сервера, удаляем..")
        driver.find_element(*InfraPageLocators.CHECK_ALL_CHECKBOX).click()
        driver.find_element(*InfraPageLocators.ACTION_BTN).click()
        driver.find_element(*InfraPageLocators.DELETE_BTN).click()
        driver.find_element(*InfraPageLocators.CONFIRM_DELETE_BTN).click()
        WebDriverWait(driver, timeout=120).until_not(EC.presence_of_element_located((By.CLASS_NAME, "q-spinner")))
        print("\nВсе серверы удалены")
    else:
        print("\nДобавленных серверов нет, добавляем сервер...")


def add_ip_server():
    driver.find_element(*InfraPageLocators.ADD_BTN).click()
    time.sleep(0.5)
    driver.find_element(*InfraPageLocators.NAME_FIELD).send_keys("test ip server")
    driver.find_element(*InfraPageLocators.TYPE).click()
    driver.find_element(*InfraPageLocators.TYPE_FIELD).click()
    driver.find_element(*InfraPageLocators.IP_ADDR_FIELD).send_keys("172.28.9.120")
    assert not driver.find_element(*InfraPageLocators.LOGIN_FIELD).is_enabled()
    driver.find_element(*InfraPageLocators.PASSWD_FIELD).send_keys("!@#$%^&*")
    driver.find_element(*InfraPageLocators.CREATE_BTN).click()
    WebDriverWait(driver, timeout=120).until_not(EC.presence_of_element_located((By.CLASS_NAME, "q-spinner")))


def check_added_ip_server():
    server_row = driver.find_element(*InfraPageLocators.SERVER_ROW).text
    assert "test ip server" in server_row
    assert "172.28.9.120 22" in server_row
    assert "Простаивает" in server_row
    assert "IP-сканер" in server_row
