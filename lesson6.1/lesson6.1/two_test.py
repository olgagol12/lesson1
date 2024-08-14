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
driver.get ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

seek_number = "[value= '5']"
number = driver.find_element(By.CSS_SELECTOR, seek_number).clear()

seek_time = "[id = 'delay']"
time = driver.find_element(By.CSS_SELECTOR, seek_time)
time.send_keys("45")


seek_seven = '//span[text()="7"]'
seven = driver.find_element(By.XPATH,seek_seven).click()

seek_plus = '//span[text()="+"]'
plus = driver.find_element(By.XPATH,seek_plus).click()

seek_eight = '//span[text()="8"]'
eight = driver.find_element(By.XPATH,seek_eight).click()

seek_equals = '//span[text()="="]'
equals= driver.find_element(By.XPATH,seek_equals).click()

wait = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
result = driver.find_element(By.CLASS_NAME, "screen").text


def test_second():
    assert result == "15"

driver.quit()