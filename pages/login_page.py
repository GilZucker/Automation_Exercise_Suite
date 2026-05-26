from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class LoginPage(BasePage):

    # Login locators

    EMAIL_FIELD = (By.CSS_SELECTOR, "[data-qa='login-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-qa='login-password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "[data-qa='login-button']")
    LOGOUT_BTN = (By.XPATH, "//*[@href='/logout']")

    # Signup locators

    NAME_FIELD = (By.CSS_SELECTOR, "[data-qa='signup-name']")
    NEW_EMAIL = (By.CSS_SELECTOR, "[data-qa='signup-email']")
    SIGN_UP = (By.CSS_SELECTOR, "[data-qa='signup-button']")

    # Signup Account Information locators

    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    ACCOUNT_PASS = (By.CSS_SELECTOR, "[data-qa='password']")
    DAYS_DD = (By.ID, "days")
    MONTHS_DD = (By.ID, "months")
    YEARS_DD = (By.ID, "years")
    NEWSLETTER_BOX = (By.CSS_SELECTOR, "[name='newsletter']")
    OFFER_BOX = (By.CSS_SELECTOR, "[name='optin']")
    FIRST_NAME = (By.CSS_SELECTOR, "[data-qa='first_name']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-qa='last_name']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-qa='address']")
    COUNTRY_DD = (By.CSS_SELECTOR, "[data-qa='country']")
    STATE = (By.CSS_SELECTOR, "[data-qa='state']")
    CITY = (By.CSS_SELECTOR, "[data-qa='city']")
    ZIP_CODE = (By.CSS_SELECTOR, "[data-qa='zipcode']")
    MOBILE_NUM = (By.CSS_SELECTOR, "[data-qa='mobile_number']")
    SUBMIT_FORM = (By.CSS_SELECTOR, "[data-qa='create-account']")






    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def signup(self, name, email):
        self.type_text(self.NAME_FIELD, name)
        self.type_text(self.NEW_EMAIL, email)
        self.click(self.SIGN_UP)

    def account_info(self, password):
        self.type_text(self.ACCOUNT_PASS, password)

    def select_gender(self, gender):
        if gender == "male":
            self.click(self.GENDER_MALE)
        elif gender == "female":
            self.click(self.GENDER_FEMALE)

    def select_dob(self, day, month, year):
        Select(self.find(self.DAYS_DD)).select_by_visible_text(day)
        Select(self.find(self.MONTHS_DD)).select_by_visible_text(month)
        Select(self.find(self.YEARS_DD)).select_by_visible_text(year)


    def choose_checkboxes(self):
        self.click(self.NEWSLETTER_BOX)
        self.click(self.OFFER_BOX)

    def address_info(self, first_name, last_name, address, state, city, zip_code, mobile_number):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.ADDRESS_FIELD, address)
        self.type_text(self.STATE, state)
        self.type_text(self.CITY, city)
        self.type_text(self.ZIP_CODE, zip_code)
        self.type_text(self.MOBILE_NUM, mobile_number)


    def select_country(self, country):
        Select(self.find(self.COUNTRY_DD)).select_by_visible_text(country)


    def submit_form(self):
        self.click(self.SUBMIT_FORM)

    def login(self, email, password):
        self.type_text(self.EMAIL_FIELD, email)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)

    def logout(self):
        self.click(self.LOGOUT_BTN)

    def quick_signup(self, email):
        self.signup("Test User", email)
        self.select_gender("male")
        self.account_info("Qwerty3!#")
        self.select_dob("1", "January", "1990")
        self.choose_checkboxes()
        self.address_info("Test", "User", "123 Street", "AL", "City", "12345", "1234567890")
        self.select_country("United States")
        self.submit_form()


        










