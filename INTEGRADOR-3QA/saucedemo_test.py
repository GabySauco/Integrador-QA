import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import HtmlTestRunner

class SauceDemoTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_and_sort(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # CASO 1: Iniciar sesión y ordenar productos
        # Iniciar sesión
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Ordenar productos por precio de menor a mayor
        sort_select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_select.select_by_visible_text("Price (low to high)")

        # Verificar que los precios estén en orden de menor a mayor
        prices_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text.replace("$", "")) for price in prices_elements]
        sorted_prices = sorted(prices)
        self.assertEqual(prices, sorted_prices, "Los precios no están ordenados de menor a mayor")

    def test_add_items_and_checkout_errors(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # CASO 2: Agregar productos y verificar errores en el checkout.
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verificar que los productos están en el carrito
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.assertEqual(len(cart_items), 1, "El producto no fue añadido al carrito correctamente")

        # Proceder al checkout
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "continue").click()

        # Verificar errores en el formulario
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Error: Last Name is required", error_message, "No se muestra el error de apellido requerido")

        # Llenar apellido, verificar siguiente error
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "continue").click()

        error_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Error: Postal Code is required", error_message, "No se muestra el error de código postal requerido")

    def test_add_remove_items_and_complete_purchase(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # CASO 3: Agregar, remover productos y completar la compra
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Remover el producto
        self.driver.find_element(By.CLASS_NAME, "cart_button").click()
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.assertEqual(len(cart_items), 0, "El carrito no está vacío")

        # Agregar dos productos
        self.driver.find_element(By.ID, "continue-shopping").click()
        add_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")[:2]
        for button in add_buttons:
            button.click()

        # Verificar que los productos están en el carrito
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.assertEqual(len(cart_items), 2, "No se agregaron correctamente los productos")

        # Completar la compra
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()

        # Verificar que la compra fue realizada
        success_message = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        self.assertEqual(success_message, "THANK YOU FOR YOUR ORDER", "La compra fue completada correctamente")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
