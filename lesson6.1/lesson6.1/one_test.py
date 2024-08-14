import pytest
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get (" https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


seek_fist_name = "[name= first-name ]"
fist_name = driver.find_element(By.CSS_SELECTOR, seek_fist_name)
fist_name.send_keys("Иван")
#фамлия
seek_last_name = "[name= last-name ]"
last_name = driver.find_element(By.CSS_SELECTOR, seek_last_name)
last_name.send_keys("Петров") 

#адрес
seek_address = "[name = address]"
address = driver.find_element(By.CSS_SELECTOR, seek_address)
address.send_keys("Ленина, 55-3") 

#почта 
seek_mail = "[name = e-mail]"
mail = driver.find_element(By.CSS_SELECTOR, seek_mail)
mail.send_keys("test@skypro.com") 

#телефон 
seek_phone = "[name = phone]"
phone = driver.find_element(By.CSS_SELECTOR, seek_phone) 
phone.send_keys("+7985899998787") 

#zip оставить пустым
seek_zip_code = "[name = zip-code]"
zip_code = driver.find_element(By.CSS_SELECTOR, seek_zip_code) 
zip_code.send_keys ("")

#город
seek_city = "[name = city]"
city = driver.find_element(By.CSS_SELECTOR, seek_city) 
city.send_keys ("Москва")

#страна
seek_country = "[name = country]"
country = driver.find_element(By.CSS_SELECTOR, seek_country) 
country.send_keys ("SkyPor")

#рабщта 
seek_job_position = "[name = job-position]"
job_position = driver.find_element(By.CSS_SELECTOR, seek_job_position ) 
job_position.send_keys ("QA")

#компания
seek_company = "[name = company]"
company = driver.find_element(By.CSS_SELECTOR, seek_company ) 
company.send_keys ("SkyPor")

#кнопка 
seek_button = "[type = 'submit']"
button = driver.find_element(By.CSS_SELECTOR, seek_button).click()

def test_first():
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "first-name"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "last-name"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "address"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "e-mail"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "phone"]').get_attribute("class")
    assert "danger" in  driver.find_element(By.CSS_SELECTOR, '[id = "zip-code"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "city"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "country"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "job-position"]').get_attribute("class")
    assert "success" in  driver.find_element(By.CSS_SELECTOR, '[id = "company"]').get_attribute("class")
