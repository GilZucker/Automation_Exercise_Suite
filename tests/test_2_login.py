from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage



class TestLogin:
    def test_login(self, driver):
        wait = WebDriverWait(driver, 10)
        login_page = LoginPage(driver)
        driver.get("https://automationexercise.com/login")

        # Read from file
        with open("test_user.txt", "r") as f:
            email = f.read()

        login_page.login(email, "Qwerty3!#")


        logged_in = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-child(4) > a")))
        assert logged_in.text == "Logout",  "❌ Couldn't reach the page"
        print("✅ Successfully logged in!")

    def test_logout(self, driver):
        wait = WebDriverWait(driver, 10)
        login_page = LoginPage(driver)
        driver.get("https://automationexercise.com/login")

        with open("test_user.txt", "r") as f:
            email = f.read()

        login_page.login(email, "Qwerty3!#")
        login_page.logout()

        # Assert you're back on login page
        assert "login" in driver.current_url, "❌ Logout failed"
        print("✅ Logged out successfully!")




















