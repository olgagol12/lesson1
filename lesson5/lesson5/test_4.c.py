from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get("http://the-internet.herokuapp.com/entry_ad")


seek_close =  "[class = 'modal-footer']"
close =  driver.find_element(By.CSS_SELECTOR, seek_close)
close.click()

sleep(20)