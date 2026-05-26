from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.searching_item import SearchItem


class TestSearching:

    def test_search_and_add(self, driver):
        wait = WebDriverWait(driver, 10)


        # 1. Login
        login_page = LoginPage(driver)
        driver.get("https://automationexercise.com/login")
        with open("test_user.txt", "r") as f:
            email = f.read()
        login_page.login(email, "Qwerty3!#")

        # 2. Close ad if appears
        try:
            close_ad = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".fc-button.fc-cta-consent")
            ))
            close_ad.click()
        except:
            pass

        # 3. Search flow
        search = SearchItem(driver)
        search.click_on_the_products_btn()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='search']")))
        search.click_search_bar()
        search.clear_field()
        search.typing_item_name("Green")
        search.click_search_btn()

        # 4. Add to cart
        search.hover_and_add_to_cart("Green Side Placket Detail T-Shirt")

        # 5. Assert
        popup = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h4[contains(text(), 'Added')]")
        ))
        assert "Added" in popup.text, "❌ Item not added to cart"
        print("✅ Item added to cart successfully!")
