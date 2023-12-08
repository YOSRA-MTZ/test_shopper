# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from seleniumpagefactory import PageFactory


# class BasePage(PageFactory):
    
#     def __init__(self,driver):
#         super().__init__()
#         self.driver=driver
#         self.wait=WebDriverWait(self.driver,10)
    
#     def wait_page_loaded(self,url):
#         self.wait.until(ec.url_to_be(url))
        
#     def wait_element_present(self,element):
#         self.wait.until(ec.presence_of_all_elements_located(element))

class BasePage:
    def __init__(self, driver):
        self.driver = driver