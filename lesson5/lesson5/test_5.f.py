from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://ya.ru")
driver.get ("http://the-internet.herokuapp.com/inputs")

seek_number = "[type = number]"
number = driver.find_element(By.CSS_SELECTOR, seek_number)
number.c 
sleep (5)
number.clear()
sleep (5)
number.send_keys("999") 
sleep (20)