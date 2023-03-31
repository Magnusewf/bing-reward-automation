from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
alfabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

driver = webdriver.Edge()
driver.get('http://bing.com/')

time.sleep(1.5)
button = driver.find_element(By.ID,"bnp_btn_accept")
button.click()
i=input("Please login then hit enter")
for _ in range(30):
    search_box = driver.find_element(By.ID,"sb_form_q")
    search_box.clear()
    search_box.send_keys(alfabet[random.randint(0,len(alfabet)-1)]+alfabet[random.randint(0,len(alfabet)-1)]+alfabet[random.randint(0,len(alfabet)-1)]+alfabet[random.randint(0,len(alfabet)-1)]+alfabet[random.randint(0,len(alfabet)-1)]+ Keys.RETURN)
    time.sleep(0.5)
    driver.back()
    time.sleep(0.5)
