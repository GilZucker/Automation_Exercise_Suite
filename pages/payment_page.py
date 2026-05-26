from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





class PaymentPage(BasePage):
    # Category locators

    NAME = (By.XPATH, "//input[@name='name_on_card']")
    CARD = (By.XPATH, "//input[@name='card_number']")
    CVC = (By.XPATH, "//input[@name='cvc']")
    EXPIRATION_MONTH = (By.XPATH, "//input[@name='expiry_month']")
    EXPIRATION_YEAR = (By.XPATH, "//input[@name='expiry_year']")
    CONFIRM_ORDER = (By.XPATH, "//button[contains(@class, 'form-control btn btn-primary submit-button')]")

    ORDER_SUCCESS_MSG = (By.XPATH, "//p[text()='Congratulations! Your order has been confirmed!']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[data-qa='continue-button']")
    VIEW_CART = (By.XPATH, "//div[@class='modal-content']//a[contains(., 'View Cart')]")




    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def fill_payment_details(self, name, card_number, cvc, month, year):
        self.type_text(self.NAME, name)
        self.type_text(self.CARD, card_number)
        self.type_text(self.CVC, cvc)
        self.type_text(self.EXPIRATION_MONTH, month)
        self.type_text(self.EXPIRATION_YEAR, year)

    def click_pay_and_confirm(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.CONFIRM_ORDER))
        self.click(self.CONFIRM_ORDER)

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.ORDER_SUCCESS_MSG))
        return self.get_text(self.ORDER_SUCCESS_MSG)

    def click_on_continue(self):
        self.click(self.CONTINUE_BTN)

    def click_the_cart_btn(self):
        self.click(self.VIEW_CART)


