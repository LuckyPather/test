from selenium.common import NoAlertPresentException, NoSuchElementException

from fixture import browser


def is_element_present(how, what):
    try:
        browser.driver.find_element(how, what)
    except NoSuchElementException as e:
        return False
    return True


def is_alert_present():
    try:
        browser.driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


# def close_alert_and_get_its_text():
#     try:
#         alert = browser.driver.switch_to_alert()
#         alert_text = alert.text
#         if self.accept_next_alert:
#             alert.accept()
#         else:
#             alert.dismiss()
#         return alert_text
#     finally:
#         self.accept_next_alert = True
