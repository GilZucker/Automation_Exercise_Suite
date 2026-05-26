from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




class ProductsPage(BasePage):
    # Category locators

    PRODUCTS_BTN = (By.XPATH, "//*[@href='/products']")
    SEARCH_BAR = (By.CSS_SELECTOR, "[name='search']")
    SEARCH_BTN = (By.CSS_SELECTOR, ".fa.fa-search")
    VIEW_CART = (By.XPATH, "//div[@class='modal-content']//a[contains(., 'View Cart')]")


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def click_products_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.PRODUCTS_BTN))
        self.click(self.PRODUCTS_BTN)

    def clear_search_bar(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_BAR))
        self.clear(self.SEARCH_BAR)

    def typing_item_name(self, text):
        self.type_text(self.SEARCH_BAR, text)

    def click_search_btn(self):
        self.click(self.SEARCH_BTN)


    def hover_and_add_to_cart(self, product_name):
        product = self.driver.find_element(By.XPATH,
                                           f"//div[@class='product-image-wrapper'][.//p[text()='{product_name}']]")

        ActionChains(self.driver).move_to_element(product).perform()

        wait = WebDriverWait(self.driver, 15)
        add_btn = wait.until(EC.visibility_of_element_located((
            By.XPATH, f"[p[text()='{product_name}']]//*[@class='btn btn-default add-to-cart']")))
        try:
            add_btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", add_btn)

    def click_view_cart(self):
        self.click(self.VIEW_CART)


















