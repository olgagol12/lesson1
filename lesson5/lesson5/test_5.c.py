from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get ("http://the-internet.herokuapp.com/inputs")

seek_number = "[type = number]"
number = driver.find_element(By.CSS_SELECTOR, seek_number)
number.send_keys("1000") 
sleep (5)
number.clear()
sleep (5)
number.send_keys("999") 
sleep (20)