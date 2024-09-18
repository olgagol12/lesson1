from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__ (self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
   
    def get_name(self):
        seek_fist_name = "[name= first-name]"
        fist_name = self._driver.find_element(By.CSS_SELECTOR, seek_fist_name)
        fist_name.send_keys("Иван")
   

    #фамлия
    def last_name(self):
        seek_last_name = "[name= last-name ]"
        last_name = self._driver.find_element(By.CSS_SELECTOR, seek_last_name)
        last_name.send_keys("Петров") 

    #адрес
    def address(self):
        seek_address = "[name = address]"
        address = self._driver.find_element(By.CSS_SELECTOR, seek_address)
        address.send_keys("Ленина, 55-3")

    #почта 
    def mail(self):
        seek_mail = "[name = e-mail]"
        mail = self._driver.find_element(By.CSS_SELECTOR, seek_mail)
        mail.send_keys("test@skypro.com") 

    #телефон 
    def phone(self):
        seek_phone = "[name = phone]"
        phone = self._driver.find_element(By.CSS_SELECTOR, seek_phone) 
        phone.send_keys("+7985899998787") 

    #zip оставить пустым
    def zip(self):
        seek_zip_code = "[name = zip-code]"
        zip_code = self._driver.find_element(By.CSS_SELECTOR, seek_zip_code) 
        zip_code.send_keys ("")

    #город
    def city(self):
        seek_city = "[name = city]"
        city = self._driver.find_element(By.CSS_SELECTOR, seek_city) 
        city.send_keys ("Москва")

    #страна
    def country(self):
        seek_country = "[name = country]"
        country = self._driver.find_element(By.CSS_SELECTOR, seek_country) 
        country.send_keys ("SkyPor")

    #рабщта 
    def job(self):
        seek_job_position = "[name = job-position]"
        job_position = self._driver.find_element(By.CSS_SELECTOR, seek_job_position ) 
        job_position.send_keys ("QA")

    #компания
    def company(self):
        seek_company = "[name = company]"
        company = self._driver.find_element(By.CSS_SELECTOR, seek_company ) 
        company.send_keys ("SkyPor")

    #кнопка 
    def button(self):
        seek_button = "[type = 'submit']"
        button = self._driver.find_element(By.CSS_SELECTOR, seek_button)
        button.click()



