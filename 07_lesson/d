import pytest
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get ("https://www.saucedemo.com/")

username= driver.find_element (By.ID, "user-name").send_keys("standard_user")

password = driver.find_element (By.ID, "password").send_keys ("secret_sauce")

loginbutton = driver.find_element (By.ID, "login-button").click()

sleep(5)

saucelabsbackpack=driver.find_element (By.ID,"add-to-cart-sauce-labs-backpack").click()

saucelabsboltshirt = driver.find_element (By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()

saucelabsonesie = driver.find_element (By.ID,"add-to-cart-sauce-labs-onesie").click()

sleep(5)
korsina = driver.find_element (By.CSS_SELECTOR, "[data-test = shopping-cart-link]").click()
sleep(5)
checkout = driver.find_element (By.ID,"checkout").click()
sleep(5)
firstname = driver.find_element (By.ID,"first-name").send_keys("Света")
lastname = driver.find_element (By.ID,"last-name").send_keys("Барская")
postalcode = driver.find_element (By.ID,"postal-code").send_keys("309085")

continu = driver.find_element (By.ID,"continue").click()
sleep(5)

totallabel = driver.find_element (By.CSS_SELECTOR, "[data-test=total-label]").text


def test_third():
    assert totallabel == "Total: $58.29"

driver.quit()