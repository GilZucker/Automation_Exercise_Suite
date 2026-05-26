from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def clean_ads(self):
        """מוחק לחלוטין את הפרסומות העקשניות של גוגל כולל ה-Shadow DOM מהשורש"""
        js_script = """
        // 1. מחיקת ה-ins הראשי שמחזיק את ה-Shadow DOM (החץ המעצבן)
        document.querySelectorAll('ins.adsbygoogle-noablate, ins.adsbygoogle').forEach(el => el.remove());

        // 2. מחיקת iframes ופרסומות קופצות אחרות של גוגל
        document.querySelectorAll('iframe[id^="aswift_"], iframe[id^="google_ads_"], div[id^="google_ads_"]').forEach(el => el.remove());

        // 3. שחרור נעילת גלילה אם קיימת
        document.body.style.overflow = 'auto';
        document.documentElement.style.overflow = 'auto';
        """
        try:
            self.driver.execute_script(js_script)
        except Exception:
            pass  # מונע מהטסט לקרוס אם ה-JS נכשל מסיבה כלשהי

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        # 1. מנקים את הפרסומות מהמסך כדי שלא יחסמו את הכפתור
        self.clean_ads()

        # 2. מוצאים את האלמנט ושומרים אותו במשתנה element
        element = self.find(locator)

        try:
            # 3. מנסים את הקליק הרגיל של סלניום
            element.click()
        except Exception:
            # 4. אם הקליק נחסם, אנחנו עוקפים את החסימה באמצעות JS
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()