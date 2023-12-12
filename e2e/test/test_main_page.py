import time
from pages import main_page
from fixture.browser import full_login


def test_add_obj():
    full_login("http://localhost/", "admin", "12345678")
    time.sleep(5)
    link = 'https://www.google.com/maps/place/%D0%AD%D0%B9%D1%84%D0%B5%D0%BB%D0%B5%D0%B2%D0%B0+%D0%B1%D0%B0%D1%88%D0' \
           '%BD%D1%8F/@48.8589384,2.2646349,' \
           '12z/data=!4m6!3m5!1s0x47e66e2964e34e2d:0x8ddca9ee380ef7e0!8m2!3d48.8583701!4d2.2944813!16zL20vMDJqODE?hl' \
           '=ru&entry=ttu'
    main_page.add_obj(name="AUTOTEST", period="12", link=link, info="АВТОТЕСТ")
    time.sleep(1)


def test_action_with_obj():
    main_page.add_in_favorites()
    main_page.start_active_monitoring()
    main_page.start_collection_data()
    main_page.stop_collection_data()
    time.sleep(1)


def test_edit_obj():
    main_page.edit_obj()
    main_page.check_edit_obg()
    time.sleep(2)
    main_page.delete_obj()


def test_add_obj_map():
    full_login('https://localhost/', 'admin', '12345678')
    time.sleep(2)
    main_page.add_obj_map('Test', '12')
    main_page.check_added_obj_map('Test', '12')
    main_page.delete_obj()