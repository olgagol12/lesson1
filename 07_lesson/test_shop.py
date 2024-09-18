import pytest
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from ShopPage import SPage




def test():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop_page = SPage(driver)
    shop_page.name()
    shop_page.word()
    shop_page.login()
    shop_page.labsbackpack()
    shop_page.labsboltshirt()
    shop_page.labsonesie()
    shop_page.korsina()
    shop_page.checkout()
    shop_page.first()
    shop_page.last()
    shop_page.postalcode()
    shop_page.continu()
    shop_page.totallabel()
    tol = shop_page.totallabel()
    assert tol == "Total: $58.29"