from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
import uuid
unique_email = f"testuser_{uuid.uuid4()}@guerrillamail.com"


class TestSignUp:
    def test_signup(self, driver):
        wait = WebDriverWait(driver, 10)
        login_page = LoginPage(driver)
        driver.get("https://automationexercise.com/login")

        unique_email = f"testuser_{uuid.uuid4()}@guerrillamail.com"
        login_page.signup("Test User", unique_email)

        with open("test_user.txt", "w") as f:
            f.write(unique_email)


        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-form")))
        element = driver.find_element(By.CSS_SELECTOR, ".login-form > :nth-child(1)")
        assert element.text == "ENTER ACCOUNT INFORMATION", "❌ Couldn't reach the page"
        print("✅ Reached the signup page!")

        # *** Choosing Gender ***
        login_page.select_gender("male")

        # *** Choosing Password ***
        login_page.account_info("Qwerty3!#")

        # *** Choosing Date Of Birth ***
        login_page.select_dob("31", "March", "1980")


        # *** Selecting Checkboxes ***
        login_page.choose_checkboxes()


        # *** Filling the text fields ***
        login_page.address_info("Muffin", "Man", "Drury Lane", "AL", "Duloc", "123312", "972504877785")

        # *** Filling the country field ***
        login_page.select_country("United States")

        # *** Clicking the submit ***
        login_page.submit_form()



        final_massage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='account-created']")))
        assert final_massage.text == "ACCOUNT CREATED!", "❌ An Error Occurred"
        print("✅ The account has been created successfully!")

        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-qa='continue-button']")
        )).click()




























