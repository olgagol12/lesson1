import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

# с заглавной буквы
def test_capitilize():
    #позитивные
    assert stringUtils.capitilize("skypro") == "Skypro"
    assert stringUtils.capitilize("привет, мир") == "Привет, мир"
    assert stringUtils.capitilize("999") == "999"
    #негативные
    assert stringUtils.capitilize('') == ''
    assert stringUtils.capitilize(' ') == ' '
    assert stringUtils.capitilize("999uuu") == "999uuu"

def test_trim():
    #позитивные
    assert stringUtils.trim("  skypro") == "skypro"
    assert stringUtils.trim("skypro") == "skypro"
    assert stringUtils.trim(" 12skypro") == "12skypro"
    #негативные
    assert stringUtils.trim("") == ""

def test_to_list():
    #позитивные
    assert stringUtils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert stringUtils.to_list("1:2:3", ":") == ["1", "2", "3"]
    #негативные
    assert stringUtils.to_list("") == []
       
def test_contains():
    #позитивные
    assert stringUtils.contains("SkyPro", "S") == True
    assert stringUtils.contains("SkyPro", "U") == False
    #негативные
    assert stringUtils.contains("SkyPro", "") == True
    assert stringUtils.contains(" ", " ") == True
    assert stringUtils.contains(" ", "U") == False
    assert stringUtils.contains("", "U") == False
    assert stringUtils.contains("", "") == True

def test_delete_symbol():
    #позитивные
    assert stringUtils.delete_symbol("SkyPro", "k") == "SyPro"
    assert stringUtils.delete_symbol("SkyPro", "Pro") == "Sky"
    #негативные
    assert stringUtils.delete_symbol("SkyPro", " ") == "SkyPro"
    assert stringUtils.delete_symbol(" ", " ") == ""
    assert stringUtils.delete_symbol(" SkyPro", " ") == "SkyPro"

def test_starts_with():
    #позитивные
    assert stringUtils.starts_with("SkyPro", "k") == False
    assert stringUtils.starts_with("SkyPro", "S") == True
    assert stringUtils.starts_with("1SkyPro1", "1") == True
    #негативные
    assert stringUtils.starts_with(" SkyPro", " ") == True
    assert stringUtils.starts_with(" ", "h") == False
    assert stringUtils.starts_with(" ", " ") == True
    assert stringUtils.end_with("", "") == True
   
 
def test_end_with():
    #позитивные
    assert stringUtils.end_with("SkyPro", "k") == False
    assert stringUtils.end_with("SkyPro", "o") == True
    assert stringUtils.end_with("SkyPro ", " ") == True
    assert stringUtils.end_with("SkyPro1", "1") == True
    #негативные
    assert stringUtils.end_with(" ", " ") == True
    assert stringUtils.end_with(" ", " b") == False
    assert stringUtils.end_with("", "") == True
    
   
def test_is_empty():
    #позитивные
    assert stringUtils.is_empty("SkyPro") == False
    assert stringUtils.is_empty("") == True
    assert stringUtils.is_empty(" ") == True
    assert stringUtils.is_empty("12") == False
    #негативные
    assert stringUtils.is_empty(" 12") == False
    assert stringUtils.is_empty("hhh ") == False
        


def test_list_to_string():
    #позитивные
    assert stringUtils.list_to_string ([1,2,3,4]) == "1, 2, 3, 4"
    assert stringUtils.list_to_string (["Sggg", "hhh"]) == "Sggg, hhh"
    assert stringUtils.list_to_string (["Sggg", "hhh"]) == "Sggg, hhh"
    assert stringUtils.list_to_string (["Sggg", "hhh"], "-") == "Sggg-hhh"
    #негативные
    assert stringUtils.list_to_string ([" "]) == " "
    assert stringUtils.list_to_string ([""]) == ""







