from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

x = datetime.datetime.now()

def extract_digits(text):
    return int(''.join(filter(str.isdigit, text)))

def find_least_expensive_product(driver, product_type):
    produits = driver.find_elements(By.XPATH, f"//p[contains(text(),'{product_type}')]")
    prix = {}

    for product in produits:
        price_element = product.find_element(By.XPATH, "./following-sibling::p")
        product_price = extract_digits(price_element.text)
        prix[product] = product_price

    sorted_prix = sorted(prix.items(), key=lambda x: x[1])
    least_expensive_product = sorted_prix[0][0]

    buy_button = driver.find_element(By.XPATH, f"//p[contains(text(),'{least_expensive_product.text}')]/following-sibling::button")
    buy_button.click()

def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://weathershopper.pythonanywhere.com/")

    assert driver.current_url == "https://weathershopper.pythonanywhere.com/", "URL incorrecte"

    driver.save_screenshot(f'screenshots/screenshot-{x.year}-{x.month}-{x.day}_{x.hour}_{x.minute}_{x.second}.png')

    assert driver.title == "Current Temperature", "Titre de la page incorrect"

    moisture = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/a/button")
    sunscreen = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/a/button")

    valeur = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/span')
    value = int(valeur.text.split()[0])

    if value < 19:
        moisture.click()
        find_least_expensive_product(driver, 'Aloe')
        find_least_expensive_product(driver, 'Almond')
    else:
        sunscreen.click()
        find_least_expensive_product(driver, 'SPF-50')
        find_least_expensive_product(driver, 'SPF-30')

    carte = driver.find_element(By.XPATH, "/html/body/nav/ul/button")
    carte.click()

    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/button").click()

    driver.switch_to.frame(0)
    formulaire = [
        driver.find_element(By.ID, "email"),
        driver.find_element(By.ID, "card_number"),
        driver.find_element(By.ID, "cc-exp"),
        driver.find_element(By.ID, "cc-csc")
    ]

    creditcarte = ["y.moumtaz@mundiapolis.ma", "4242424242424242", "1224", "333"]

    def typeslowly(loc, text):
        for i in text:
            loc.send_keys(i)

    for i in range(4):
        typeslowly(formulaire[i], creditcarte[i])

    zip_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'billing-zip'))
    )
    zip_element.send_keys("24")

    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="submitButton"]'))
    )
    submit_button.click()

    time.sleep(5)
    driver.quit()

test_google_search()