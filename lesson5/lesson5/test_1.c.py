from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get ("http://the-internet.herokuapp.com/add_remove_elements/")



seek_add ="[onclick='addElement()']"
add = driver.find_element(By.CSS_SELECTOR, seek_add)
add.send_keys(Keys.ENTER)
add.send_keys(Keys.ENTER)
add.send_keys(Keys.ENTER)
add.send_keys(Keys.ENTER)
add.send_keys(Keys.ENTER)


seek_delet = "[id='elements']"
delet = driver.find_elements(By.CSS_SELECTOR, seek_delet)

for de in delet:
    print (de.text)


sleep (20)