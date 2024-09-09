import pytest
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from Page import MainPage


def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    page = MainPage(driver)
    page.get_name()
    page.last_name()
    page.address()
    page.mail()
    page.phone()
    page.zip()
    page.city()
    page.country()
    page.job()
    page.company()
    page.button()
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






