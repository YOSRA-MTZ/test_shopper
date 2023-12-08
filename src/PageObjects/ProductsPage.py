# from selenium.webdriver.common.by import By
# from src.PageObjects.base.BasePage import BasePage

# class ProductsPage(BasePage):
#     locators={
#         "cart_btn":("XPATH","/html/body/nav/ul/button")
#     }
#     def add_cheapest_to_cart(self,produit):
#         addbtns=self.driver.find_elements(By.TAG_NAME,'button')
#         prix={}
        
#         for addBtn in addbtns:
#             text=addBtn.get_attribute("onclick")
#             if produit in text:
#                 prices = text.split(',')[1].split(')')[::1]
#                 prix.append(prices[0])
#         min_prix=min(prix)
#         for addBtn in addbtns:
#             text=addBtn.get_attribute("onclick")
#             if str(min_prix) in text:
#                 addBtn.click()
        
        
#     def go_to_cart(self):
#         self.cart_btn.click_button()
        
        
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.PageObjects.base.BasePage import BasePage
class ProductsPage(BasePage):
    def get_product_prices(self, product_type):
        produits = self.driver.find_elements(By.XPATH, f"//p[contains(text(),'{product_type}')]")
        prices = {}

        for product in produits:
            price_element = product.find_element(By.XPATH, "./following-sibling::p")
            product_price = self.extract_digits(price_element.text)
            prices[product] = product_price

        sorted_prices = sorted(prices.items(), key=lambda x: x[1])
        least_expensive_product = sorted_prices[0][0]

        return least_expensive_product

    def extract_digits(self, text):
        return int(''.join(filter(str.isdigit, text)))

    def click_buy_button(self, product_name):
        buy_button = self.driver.find_element(By.XPATH, f"//p[contains(text(),'{product_name}')]/following-sibling::button")
        buy_button.click()
