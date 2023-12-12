import time

from fixture.browser import full_login
from pages import infra_page

full_login("https://172.28.9.120/", "admin", "12345678")


def test_add_ip_server():
    # Arrange
    infra_page.go_to_infra_page()
    # Act
    infra_page.check_servers_are_not_added()
    infra_page.add_ip_server()
    # Assert
    infra_page.check_added_ip_server()
