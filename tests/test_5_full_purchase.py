import time
import uuid

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.searching_item import SearchItem
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.payment_page import PaymentPage


class TestFullPurchase:

    def test_full_purchase(self, driver):
        wait = WebDriverWait(driver, 10)

        # 1. Create fresh account
        login_page = LoginPage(driver)
        driver.get("https://automationexercise.com/login")
        unique_email = f"testuser_{uuid.uuid4()}@guerrillamail.com"
        login_page.quick_signup(unique_email)



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
        item1 = "Sleeveless Unicorn"
        search.typing_item_name(item1)
        search.click_search_btn()

        # 4. Add to cart
        search.hover_and_add_to_cart("Sleeveless Unicorn Patch Gown - Pink")

        # 5. Verify product was added to cart
        popup = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h4[contains(text(), 'Added')]")
        ))
        assert "Added" in popup.text, "❌ Item not added to cart"
        print(f"✅ Item: {item1} - added to cart successfully!")

        # 1. First, clicking the button to close the module
        search.click_continue_shopping()

        # 2. Verifying that the popup disappeared
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//h4[contains(text(), 'Added')]")))

        # 6. Search for another item
        search.clear_field()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "[name='search']"), ""))
        item2 = "Colour Blocked Shirt – Sky Blue"
        search.typing_item_name(item2)
        search.click_search_btn()

        # 7. Add to cart
        search.hover_and_add_to_cart("Colour Blocked Shirt – Sky Blue")

        # 8. Assert
        popup = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h4[contains(text(), 'Added')]")
        ))
        assert "Added" in popup.text, "❌ Item not added to cart"
        print(f"✅ Item: {item2} -  added to cart successfully!")


        # 9. Go to cart and check the items
        products_page = ProductsPage(driver)
        products_page.click_view_cart()

        # 10. Checking the items inside the cart for information
        cart_page = CartPage(driver)
        result = cart_page.get_cart_items()

        # Keeping the prices as variables to use them later
        price_item1 = result[0]['price']
        price_item2 = result[1]['price']

        assert len(result) == 2, "❌ Expected 2 item!"
        print(f"✅ There are 2 items in the cart: {result[0]['name']}, Price: {result[0]['price']}, Quantity: {result[0]['quantity']}")

        # 11. Getting the information of the total price
        total = cart_page.get_total_price()
        print(f"✅ Total Price: {total}")

        # 12. Proceed to Checkout
        cart_page.proceed_to_checkout()
        print("✅ Reached the checkout page")

        # 13. Checking the delivery address info
        checkout_page = CheckoutPage(driver)
        address_text = checkout_page.get_delivery_address_text()
        assert "123 Street" in address_text, "❌ Delivery address street is missing or incorrect!"
        assert "City" in address_text, "❌ Delivery address city is missing or incorrect!"
        assert "12345" in address_text, "❌ Delivery address zip_code is missing or incorrect!"
        assert "1234567890" in address_text, "❌ Delivery address mobile number is missing or incorrect!"

        # 14. Checking the item list
        checkout_items = checkout_page.get_checkout_items()

        assert len(checkout_items) == 2, "❌ Expected 2 items in checkout! but got a different number of items!"

        # 15. Validating that the correct items appear in the checkout
        assert "Sleeveless Unicorn" in checkout_items[0]["name"], "❌ Product name is incorrect!"
        print(f"DEBUG: What is actually inside checkout_items[1]? -> {checkout_items[1]}")
        print(f"✅ The first item - {item1} is correct")

        assert checkout_items[0]["price"] == price_item1, f"❌ Expected {price_item1} but got {checkout_items[0]['price']}"
        print(f"✅ The first item's - {item1} price is correct")

        assert "1" in checkout_items[0]["quantity"], "❌ The quantity is incorrect!"
        print(f"✅ The first item's - {item1} quantity is correct")

        #==========================================================================
        assert "Sky Blue" in checkout_items[1]["name"], "❌ Product name is incorrect!"
        print(f"✅ The second item - {item2} is correct")

        assert checkout_items[1]["price"] == price_item2, f"❌ Expected {price_item2} but got {checkout_items[1]['price']}"
        print(f"✅ The second item's - {item2} price is correct")

        assert "1" in checkout_items[1]["quantity"], "❌ The quantity is incorrect!"
        print(f"✅ The second item's - {item2} quantity is correct")


        # 16. Checking Total
        checkout_total = checkout_page.get_total_price("1899")
        assert "1899" in checkout_total, f"❌ Grand total is incorrect! Expected 1899 but got {checkout_total}"
        print(f"✅ Grand Total Price in checkout is correct: {checkout_total}")


        # 17. Typing comment
        checkout_page.enter_comments("Please deliver afternoon as soon as possible!")
        print(f"✅ Added a comment to the field")

        # 18. Placing order
        checkout_page.click_place_order()

        # 19. Filling the payment form
        payment_page = PaymentPage(driver)
        payment_page.fill_payment_details("User Test", "123456789", "353", "01", "1980")

        # 20. Clicking confirm
        payment_page.click_pay_and_confirm()

        # 21. Assertion of placed order
        message = payment_page.get_success_message()
        assert "CONGRATULATIONS!" in message.upper(), f"❌ Couldn't verify the message. Got: {message}"
        print(f"✅ The message '{message}' appeared correctly")

        # 22. Clicking on continue, ahead of placed order
        payment_page.click_on_continue()

        # 23. Verifying we reached the home page
        logged_in = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-child(4) > a")))
        assert logged_in.text == "Logout", "❌ Couldn't reach the page"
        print("✅ Successfully reached the home page!")

        # 24. Click the cart button
        payment_page.click_the_cart_btn()

        empty_cart_element = driver.find_element(By.XPATH, "//b[text()='Cart is empty!']")
        assert "empty" in empty_cart_element.text, "❌ Cart is not empty after purchase!"
        print("██████████████████████████████████████████████████████████████████████")
        print("🏆 SUCCESS: E2E Purchase Flow Completed & Cart is Verified Empty! 🏆")
        print("██████████████████████████████████████████████████████████████████████")
































