
from pages.login_page import LoginPage
from utils.driver_factory import get_driver

def test_valid_login():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert "Swag Labs" in login_page.get_title()

    driver.quit()
