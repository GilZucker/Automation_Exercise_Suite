from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class SearchItem(BasePage):
    # Category locators

    PRODUCTS_BTN = (By.XPATH, "//*[@href='/products']")
    SEARCH_BAR = (By.CSS_SELECTOR, "[name='search']")
    SEARCH_BTN = (By.CSS_SELECTOR, ".fa.fa-search")


    CONTINUE_BTN_LOCATOR = (By.CSS_SELECTOR, "[data-dismiss='modal']")





    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_on_the_products_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.PRODUCTS_BTN))
        self.click(self.PRODUCTS_BTN)

    def click_search_bar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_BAR))
        self.click(self.SEARCH_BAR)

    def clear_field(self):
        self.clear(self.SEARCH_BAR)

    def typing_item_name(self, text):
        self.type_text(self.SEARCH_BAR, text)

    def click_search_btn(self):
        self.click(self.SEARCH_BTN)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_BTN_LOCATOR)


    def hover_and_add_to_cart(self, product_name):
        product_xpath = f"//div[@class='product-image-wrapper'][.//p[text()='{product_name}']]"
        product = self.driver.find_element(By.XPATH, product_xpath)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)



        ActionChains(self.driver).move_to_element(product).perform()

        btn_xpath = f"//div[@class='product-image-wrapper'][.//p[text()='{product_name}']]//a[contains(@class, 'add-to-cart')]"
        wait = WebDriverWait(self.driver, 10)
        add_btn = wait.until(EC.presence_of_element_located((By.XPATH, btn_xpath)))

        self.clean_ads()

        try:
            add_btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", add_btn)

