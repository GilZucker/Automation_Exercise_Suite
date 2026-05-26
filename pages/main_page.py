from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MainPage(BasePage):
    # Category locators

    CATEGORY_MEN = (By.XPATH, "//a[@href='#Men']")
    MEN_TSHIRTS = (By.XPATH, "//a[text()='Tshirts']")
    MAN_JEANS = (By.XPATH, "//a[text()='Jeans']")
    CATEGORY_WOMEN = (By.XPATH, "//a[@href='#Women']")
    WOMEN_DRESS = (By.XPATH, "//a[@href='#Women']//a[contains(text(), 'Dress')]")
    WOMEN_TOPS = (By.XPATH, "//div[@id='Women']//a[contains(text(), 'Tops')]")
    WOMEN_SAREE = (By.XPATH, "//a[text()='Saree']")
    CATEGORY_KIDS = (By.XPATH, "//a[@href='#Kids']")
    KIDS_DRESS = (By.XPATH, "//a[@href='#Kids']//a[contains(text(), 'Dress')]")
    KIDS_TOPS_AND_SHIRTS = (By.XPATH, "//a[@href='#Kids']//a[contains(text(), 'Tops & Shirts')]")





    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def hover_and_add_to_cart(self, product_name):
        product = self.driver.find_element(By.XPATH,
                                           f"//div[@class='product-image-wrapper'][.//p[text()='{product_name}']]")

        ActionChains(self.driver).move_to_element(product).perform()

        add_btn = product.find_element(By.CSS_SELECTOR, ".add-to-cart")
        add_btn.click()

    def click_women_category(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.CATEGORY_WOMEN))
        self.click(self.CATEGORY_WOMEN)

    def click_women_tops(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.WOMEN_TOPS))
        self.click(self.WOMEN_TOPS)






