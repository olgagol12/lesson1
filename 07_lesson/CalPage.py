from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CPage:
    def __init__ (self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def number(self):
        seek_number = "[value= '5']"
        number = self._driver.find_element(By.CSS_SELECTOR, seek_number)
        number.clear()

    def time(self):
        seek_time = "[id = 'delay']"
        time = self._driver.find_element(By.CSS_SELECTOR, seek_time)
        time.send_keys("45")

    def seven(self):
        seek_seven = '//span[text()="7"]'
        seven = self._driver.find_element(By.XPATH,seek_seven)
        seven.click()

    def plus(self):
        seek_plus = '//span[text()="+"]'
        plus = self._driver.find_element(By.XPATH,seek_plus)
        plus.click()
        
    def eigh(self):
        seek_eight = '//span[text()="8"]'
        eight = self._driver.find_element(By.XPATH,seek_eight)
        eight.click()

    def equals(self):
        seek_equals = '//span[text()="="]'
        equals= self._driver.find_element(By.XPATH,seek_equals)
        equals.click()

    def wait(self):
        wait = WebDriverWait(self._driver, 50).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result = self._driver.find_element(By.CLASS_NAME, "screen")
        result.text
        return ("15")

