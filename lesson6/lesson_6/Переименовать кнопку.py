from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get("http://uitestingplayground.com/textinput")


sleep (5)
button = driver.find_element (By.CSS_SELECTOR, "#newButtonName")
button.send_keys("SkyPro")

button_that = driver.find_element (By.CSS_SELECTOR,"#updatingButton").click()

button_that = driver.find_element (By.CSS_SELECTOR,"#updatingButton").text

print(button_that)
sleep (10)
driver.quit()