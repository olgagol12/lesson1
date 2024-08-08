from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru")
driver.get("http://www.uitestingplayground.com/ajax")


driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

seek_green = driver.find_element(By.CSS_SELECTOR, "#content")
green = seek_green.find_element(By.CSS_SELECTOR, ".bg-success").text

print(green)

driver.quit()