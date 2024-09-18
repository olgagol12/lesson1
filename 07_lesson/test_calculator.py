import pytest
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from CalPage import CPage



def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    cal_page = CPage(driver)
    cal_page.number()
    cal_page.time()
    cal_page.seven()
    cal_page.plus()
    cal_page.eigh()
    cal_page.equals()
    cal_page.wait()
    tol = cal_page.wait()
    assert tol == "15"
