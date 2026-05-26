from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





class CheckoutPage(BasePage):
    # Category locators

    DELIVERY_ADDRESS = (By.XPATH, "//ul[@class='address item box']")
    CART_ITEMS = (By.XPATH, "//tr[contains(@id, 'product')]")
    ITEM_PRICES = (By.XPATH, ".//td[contains(@class, 'cart_price')]//p")
    ITEMS_QUANTITY = (By.XPATH, ".//td[contains(@class, 'cart_quantity')]")
    ITEM_DESCRIPTION = (By.XPATH, ".//td[contains(@class, 'cart_description')]")
    TOTAL_PRICE = (By.XPATH, "//table[@class='table table-condensed']//tr[last()]//p[@class='cart_total_price']")
    COMMENT_AREA = (By.XPATH, "//textarea[contains(@class, 'form-control')]")
    GO_TO_PLACE_ORDER = (By.XPATH, "//a[contains(@class, 'check_out')]")


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_delivery_address_text(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.DELIVERY_ADDRESS))
        return self.get_text(self.DELIVERY_ADDRESS)




    def get_checkout_items(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.CART_ITEMS))
        items = self.driver.find_elements(*self.CART_ITEMS)
        result = []
        for item in items:
            name = item.find_element(*self.ITEM_DESCRIPTION)
            price = item.find_element(*self.ITEM_PRICES)
            quantity = item.find_element(*self.ITEMS_QUANTITY)

            result.append({"name": name.text, "price": price.text, "quantity": quantity.text})
        return result

    def get_total_price(self, expected_total=None):
        wait = WebDriverWait(self.driver, 10)

        # 1. Waiting for the element to appear
        total_element = wait.until(EC.presence_of_element_located(self.TOTAL_PRICE))

        # 2. Screen scrolling to the center
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", total_element)

        # 3. Printing the result output of the selenium
        print(f"\n🔍 DEBUG SCREEN: The text currently inside TOTAL_PRICE element is: '{total_element.text}'")

        # 4. Waiting
        if expected_total:
            wait.until(EC.text_to_be_present_in_element(self.TOTAL_PRICE, expected_total))

        return self.get_text(self.TOTAL_PRICE)

    def enter_comments(self, text):
        return self.type_text(self.COMMENT_AREA, text)

    def click_place_order(self):
        return self.click(self.GO_TO_PLACE_ORDER)



