# Automation Exercise - E2E Testing Suite 🚀

This repository contains a robust, industrial-grade automation testing framework built for the **Automation Exercise** website. The project implements modern automation best practices, ensuring high stability, scalability, and fast execution.

## 🛠️ Tech Stack & Architecture

- **Language:** Python 3
- **Framework:** Pytest
- **Tool:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)
- **Reporting & Logging:** Built-in Pytest logging with detailed assertions

---

## 🏗️ Core Features & Framework Architecture

The framework is structured using the **Page Object Model (POM)** to separate test logic from page-specific UI elements, making the suite highly maintainable.

* **Base Page Object:** Contains encapsulated, reusable Selenium actions (Waits, clicks, text entry, element validation) to eliminate flaky tests and avoid hardcoded `time.sleep()`.
* **Explicit Dynamic Synchronization:** Heavy reliance on `WebDriverWait` and `expected_conditions` to handle dynamic elements and asynchronous UI updates efficiently.
* **Clean Code Practices:** Highly readable locator definitions separated visually from action methods within the page classes.

---

## 🧪 Test Scenarios Covered

The suite executes 6 comprehensive test scenarios covering critical user journeys:

1. **User Sign-Up Flow:** Validates a complete new user registration.
2. **User Login Flow:** Verifies successful authentication with valid credentials.
3. **User Logout Flow:** Ensures secure session termination and redirection.
4. **Product Search & Add to Cart:** Validates search functionality and multi-item cart additions.
5. **E2E Shopping Flow:** A complete purchasing pipeline from product selection to checkout.
6. **Full Purchase End-to-End (E2E):** The ultimate integration test covering:
   - Dynamic product selection and cart validation.
   - Account creation / checkout progression.
   - Secure simulated payment form filling.
   - Order confirmation text verification.
   - **Post-purchase verification:** Automatically navigates back to ensure the user's cart has been successfully emptied after a transaction.

---

## 🚀 How to Run the Project

### 1. Prerequisites
Make sure you have Python installed, then clone the repository:
```bash
git clone [https://github.com/GilZucker/Automation_Exercise_Suite.git](https://github.com/GilZucker/Automation_Exercise_Suite.git)
cd Automation_Exercise_Suite
```


### 2. Setup Virtual Environment
python -m venv .venv

On Windows: .venv\Scripts\activate
On Mac/Linux: source .venv/bin/activate

### 3. Install Dependencies
pip install pytest selenium

### 4. Execute the Test Suite
pytest -v





