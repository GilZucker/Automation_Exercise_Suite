from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestShopping:
    def test_shopping(self, driver):
        wait = WebDriverWait(driver, 10)
        login_page = LoginPage(driver)
        driver.get("https://automationexercise.com/login")

        try:
            close_ad = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".fc-button.fc-cta-consent")
            ))
            close_ad.click()
        except:
            pass  # no popup, continue

        with open("test_user.txt", "r") as f:
            email = f.read()

        login_page.login(email, "Qwerty3!#")

        main_page = MainPage(driver)
        main_page.click_women_category()
        main_page.click_women_tops()
        main_page.hover_and_add_to_cart("Blue Top")

        wait.until(EC.visibility_of_element_located((By. CSS_SELECTOR, ".modal-header")))
        popup = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h4[contains(text(), 'Added')]")
        ))
        assert "Added" in popup.text, "❌ Item not added to cart"
        print("✅ Item added to cart successfully!")
