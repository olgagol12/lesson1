from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get("http://the-internet.herokuapp.com/login")


seek_username = "[name = username]"
username = driver.find_element(By.CSS_SELECTOR, seek_username)
username.send_keys("tomsmith")

seek_password = "[name = password]"
password= driver.find_element(By.CSS_SELECTOR, seek_password)
password.send_keys("SuperSecretPassword!")

seek_login = "[type=submit]"
login = driver.find_element(By.CSS_SELECTOR, seek_login)
login.click()

sleep(20)