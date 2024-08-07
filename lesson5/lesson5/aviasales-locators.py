from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#Локатор логотипа (html-елемент, содержащий в себе значок и слово "авиасейлс") - <тут ваш локатор>
#Локатор поля Откуда - <тут ваш локатор>
#Локатор поля Куда - <тут ваш локатор>
#Локатор поля Когда - <тут ваш локатор>
#Локатор поля Обратно - <тут ваш локатор>
#Локатор чек-бокса "Открыть Ostrovok.ru в новой вкладке" - <тут ваш локатор>
#Локатор кнопки Найти билеты - <тут ваш локатор>

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#открыли сайт 
driver.get("https://ya.ru")
driver.get ("https://www.aviasales.ru")

#Локатор логотипа (html-елемент, содержащий в себе значок и слово "авиасейлс") - <тут ваш локатор>

seek_logo = "[data-test-id = 'logo']"
logo = driver.find_element(By.CSS_SELECTOR, seek_logo)

#Локатор поля Откуда - <тут ваш локатор>
seek_otkyda = "[placeholder = 'Откуда']"
otkyda = driver.find_element(By.CSS_SELECTOR, seek_otkyda)


#Локатор поля Куда - <тут ваш локатор>
seek_where = "[placeholder = 'Куда']"
where = driver.find_element(By.CSS_SELECTOR, seek_where)

#Локатор поля Когда - <тут ваш локатор>
seek_when  = "[data-test-id = start-date-field]"
when = driver.find_element(By.CSS_SELECTOR, seek_when)

#Локатор поля Обратно - <тут ваш локатор>
seek_back  = "[data-test-id = end-date-field]"
back= driver.find_element(By.CSS_SELECTOR, seek_back)

#Локатор чек-бокса "Открыть Ostrovok.ru в новой вкладке" - <тут ваш локатор>
seek_open = "[data-test-id = no-cashback-label]"
open = driver.find_element(By.CSS_SELECTOR, seek_open)

#Локатор кнопки Найти билеты - <тут ваш локатор>
seek_ticket = ".s__Yzjov8gtTIwlOo3oK8L3"
ticket = driver.find_element(By.CSS_SELECTOR, seek_ticket)



sleep (60)