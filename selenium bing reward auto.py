from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Edge()
driver.get('http://bing.com/')

time.sleep(2)
button = driver.find_element(By.ID,"bnp_btn_accept")
button.click()
i=input("Please login then hit enter")
for _ in range(30):
    search_box = driver.find_element(By.ID,"sb_form_q")
    search_box.clear()
    search_box.send_keys("a"+ Keys.RETURN)
    time.sleep(0.5)
    driver.back()
