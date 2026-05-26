from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





class CartPage(BasePage):
    # Category locators

    CART_ITEMS = (By.XPATH, "//tr[contains(@id, 'product')]")
    ITEM_PRICES = (By.XPATH, ".//td[contains(@class, 'cart_price')]")
    ITEMS_QUANTITY = (By.XPATH, ".//td[contains(@class, 'cart_quantity')]")
    ITEM_DESCRIPTION = (By.XPATH, ".//td[contains(@class, 'cart_description')]")
    TOTAL_PRICE = (By.XPATH, "//p[@class='cart_total_price']")
    MOVE_TO_CHECKOUT = (By.XPATH, "//a[contains(@class, 'check_out')]")


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def get_cart_items(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: len(driver.find_elements(*self.CART_ITEMS)) == 2)
        wait.until(EC.visibility_of_element_located(self.CART_ITEMS))
        items = self.driver.find_elements(*self.CART_ITEMS)
        result = []
        for item in items:
            name = item.find_element(*self.ITEM_DESCRIPTION)
            price = item.find_element(*self.ITEM_PRICES)
            quantity = item.find_element(*self.ITEMS_QUANTITY)

            result.append({"name": name.text, "price": price.text, "quantity": quantity.text})
        return result

    def get_total_price(self):
        return self.get_text(self.TOTAL_PRICE)


    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.MOVE_TO_CHECKOUT)).click()



