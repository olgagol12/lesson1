from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



#Локатор кнопки Войти - <тут ваш локатор>
#Локатор кнопки Заказы - <тут ваш локатор>
#Локатор ссылки OZON Job (в футере) - <тут ваш локатор>
#Локатор выбора валюты (верхний левый угол страницы) - <тут ваш локатор>
#Локатор выпадашки Везде (в поисковой строке) - <тут ваш локатор>

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get ("https://www.ozon.ru/")

#Локатор кнопки Войти - <тут ваш локатор>
seek_comein = "[class = 'nd5_46_9']"
comein = driver.find_element(By.CSS_SELECTOR, seek_comein)

#Локатор кнопки Заказы - <тут ваш локатор>
seek_order = "[class = 'nd5_14_9']"
order = driver.find_element(By.CSS_SELECTOR, seek_order)

#Локатор ссылки OZON Job (в футере) - <тут ваш локатор>
seek_ozonjob = "[href= 'https://job.ozon.ru/?perehod=footer'][class = 'a6 d9e_9']"
ozonjob = driver.find_element(By.CSS_SELECTOR, seek_ozonjob)

#Локатор выбора валюты (верхний левый угол страницы) - <тут ваш локатор>

seek_valyta = "[data-widget='selectedCurrency']"
valyta = driver.find_element(By.CSS_SELECTOR, seek_valyta)

#Локатор выпадашки Везде (в поисковой строке) - <тут ваш локатор>

seek_vesde= "[title='Везде']"
vesde =  driver.find_element(By.CSS_SELECTOR, seek_vesde)





sleep (60)











sleep(15)
