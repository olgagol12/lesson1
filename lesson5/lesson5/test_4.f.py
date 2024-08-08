from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://ya.ru")
driver.get("http://the-internet.herokuapp.com/entry_ad")


seek_close =  "[class = 'modal-footer']"
close =  driver.find_element(By.CSS_SELECTOR, seek_close)
close.click()

sleep(20)