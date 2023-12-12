from selenium.webdriver.common.by import By


class LoginPage:
    LOGO = (By.CLASS_NAME, "login-form-header")
    LOGIN_INPUT = (By.CSS_SELECTOR, "[type='text']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[type='password']")
    LOGIN_BTN = (By.CLASS_NAME, "q-btn__content")
    ERROR_MESSAGE = (By.CLASS_NAME, "q-notification__message")


class MainPage:
    LOGO = (By.CLASS_NAME, "ui-title")
    TAB_TITLE = (By.CSS_SELECTOR, '#tab_tile')
    ADD_BUTTON = (By.ID, 'button_open_dialog')
    CLOSE_MODAL_WINDOW = (By.CSS_SELECTOR,
                          '#button_close > span.q-btn__content.text-center.col.items-center.q-anchor--skip.justify-center.row > span')
    NAME_OBJ = (By.CSS_SELECTOR, '#input_text_object > label')
    PERIOD = (By.CSS_SELECTOR, '#input_text_object_period > label')
    WIDTH = (By.XPATH, '//*[@id="q-portal--dialog--3"]/div/div[2]/div/div[2]/form/div[3]/label[1]')
    LONGITUDE = (By.XPATH, '//*[@id="q-portal--dialog--3"]/div/div[2]/div/div[2]/form/div[3]/label[2]')
    MAP_LINK = (By.CSS_SELECTOR, '#input_text_url > label')
    COMMENT = (By.CSS_SELECTOR, '#input_text_comment > label')
    COMMENT2 = (By.XPATH, "/html/body/div[1]/div/div[2]/main/div/div/div[2]/div/div/div[1]/form/label[3]/div/div["
                          "1]/div/textarea")
    ADD_BUTTON_OBJ = (By.CSS_SELECTOR, '#button_submit_dialog')
    CANCEL_BUTTON_OBJ = (By.XPATH, '//*[@id="q-portal--dialog--5"]/div/div[2]/div/div[3]/button[1]/span[2]/span')
    GROUP_OF_EVENT = (By.XPATH, '//*[@id="q-app"]/div/div[2]/main/div/div/div[2]/div/div/div/div[2]')
    FAVOURITES = (By.CSS_SELECTOR, '#button_pin')
    INTENSIVE_MONITORING = (By.CSS_SELECTOR, '#button_observation')
    STOP_COLLECTING_DATA = (By.CSS_SELECTOR, '#button_action')
    EDIT = (By.CSS_SELECTOR, '#button_edit')
    LOOK_BUTTON = (By.CSS_SELECTOR, '#button_look')
    PARAMETERS = (By.XPATH, '//*[@id="q-app"]/div/div[2]/main/div/div/div[1]/div[1]/div/div/a[4]/div[2]/div')
    DELETE_BTN = (By.XPATH, '//*[@id="button_delete"]')
    CHECK_NAME = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/label/div/div[1]/div/input')
    CHECK_PERIOD = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/label/div/div[1]/div[2]/input')
    CHECK_COMMENT = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[7]/label/div/div[1]/div/textarea')


class Map:
    TAB_MAP = (By.CSS_SELECTOR, '#tab_map')
    MAP = (By.CSS_SELECTOR, '#q-app > div > div.q-page-container > main > div > div > div.flex.col.column > div > div '
                            '> div')


class InfraPageLocators:
    INFRA_PAGE_BTN = (By.CSS_SELECTOR, "[href='/infra']")
    ADD_BTN = (By.XPATH, "//*[contains(text(), 'Добавить')]")
    NAME_FIELD = (By.CSS_SELECTOR, "[placeholder='Наименование сервера']")
    TYPE = (By.CLASS_NAME, "grey-6")
    TYPE_FIELD = (By.XPATH, "//*[contains(text(), 'IP-сканер')]")
    IP_ADDR_FIELD = (By.CSS_SELECTOR, "[placeholder='111.111.111.111']")
    PORT_FIELD = (By.CSS_SELECTOR, "[aria-label='Порт']")
    LOGIN_FIELD = (By.CSS_SELECTOR, "[aria-label='Логин']")
    PASSWD_FIELD = (By.CSS_SELECTOR, "[placeholder='Пароль сервера']")
    CREATE_BTN = (By.XPATH, "//*[contains(text(), 'Создать')]")
    INFRA_TABLE_EMPTY = (By.CLASS_NAME, "ui-no-data")
    CHECK_ALL_CHECKBOX = (By.CLASS_NAME, "q-checkbox__bg")
    ACTION_BTN = (By.XPATH, "//*[contains(text(), 'Действия')]")
    DELETE_BTN = (By.CSS_SELECTOR, ".q-item__section.text-negative")
    CONFIRM_DELETE_BTN = (By.XPATH, "//*[contains(text(), 'Удалить')]")
    SPINNER = (By.CLASS_NAME, "q-spinner")
    SERVER_ROW = (By.CSS_SELECTOR, "tbody")
