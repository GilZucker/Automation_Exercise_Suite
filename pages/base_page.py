from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def clean_ads(self):
        """ Deleting the persistent ads from Google, including the Shadow DOM"""
        js_script = """
        // 1. Remove the main 'ins' element holding the Shadow DOM (the annoying arrow ad)
        document.querySelectorAll('ins.adsbygoogle-noablate, ins.adsbygoogle').forEach(el => el.remove());

        // 2. Remove any Google ad iframes and overlay wrappers
        document.querySelectorAll('iframe[id^="aswift_"], iframe[id^="google_ads_"], div[id^="google_ads_"]').forEach(el => el.remove());

        // 3. Unlock page scrolling if restricted by ads
        document.body.style.overflow = 'auto';
        document.documentElement.style.overflow = 'auto';
        """
        try:
            self.driver.execute_script(js_script)
        except Exception:
            pass  # Prevents test from crashing if JS execution fails for any reason

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        # 1. Clear active ads from the viewport to prevent blocking the element
        self.clean_ads()

        # 2. Locate the element and store it in a variable
        element = self.find(locator)

        try:
            # 3. Attempt standard Selenium click action
            element.click()
        except Exception:
            # 4. If the standard click is intercepted/blocked, bypass via JavaScript executor
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()