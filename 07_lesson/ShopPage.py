from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class SPage:
    def __init__ (self, driver):
        self._driver = driver
        self._driver.get(" https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()


    def name(self):
        username = self._driver.find_element (By.ID, "user-name")
        username.send_keys("standard_user")

    def word(self):
        password = self._driver.find_element (By.ID, "password")
        password.send_keys ("secret_sauce")
    def login(self):
        loginbutton = self._driver.find_element (By.ID, "login-button")
        loginbutton.click()
    sleep(20)

    def labsbackpack (self):
        saucelabsbackpack= self._driver.find_element (By.ID,"add-to-cart-sauce-labs-backpack")
        saucelabsbackpack.click()

    def labsboltshirt (self):
        saucelabsboltshirt = self._driver.find_element (By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
        saucelabsboltshirt.click()
    
    def labsonesie (self):
        saucelabsonesie = self._driver.find_element (By.ID,"add-to-cart-sauce-labs-onesie")
        saucelabsonesie.click()
    sleep(20)
    
    def korsina(self):
        korsina = self._driver.find_element (By.CSS_SELECTOR, "[data-test = shopping-cart-link]")
        korsina.click()
    sleep(10)
    def checkout(self):
        checkout = self._driver.find_element (By.ID,"checkout")
        checkout.click()

    sleep(10)
    def first(self):
        firstname =self._driver.find_element (By.ID,"first-name")
        firstname.send_keys("Света")

    def last (self):
        lastname = self._driver.find_element (By.ID,"last-name")
        lastname.send_keys("Барская")

    def postalcode(self):
        postalcode = self._driver.find_element (By.ID,"postal-code")
        postalcode.send_keys("309085")

    def continu(self):
        continu = self._driver.find_element (By.ID,"continue")
        continu.click()

    sleep(10)

    def  totallabel(self):
        totallabel = self._driver.find_element (By.CSS_SELECTOR, "[data-test=total-label]")
        totallabel.text
        return ("Total: $58.29")




