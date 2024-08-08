from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get("http://uitestingplayground.com/dynamicid")

seek_blue = "[class = 'btn btn-primary']"
blue = driver.find_element(By.CSS_SELECTOR, seek_blue)
blue.send_keys(Keys.ENTER)
blue.send_keys(Keys.ENTER)
blue.send_keys(Keys.ENTER)

sleep(20)