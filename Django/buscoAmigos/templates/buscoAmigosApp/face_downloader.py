import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import os


# driver = webdriver.Chrome()
# driver.get("https://this-person-does-not-exist.com/en")
# driver.set_window_size(1280, 1440)
# time.sleep(2)

# chrome_options = webdriver.ChromeOptions()
# prefs = {'download.default_directory' : 'buscoAmigos/templates/buscoAmigosApp/Images'}
# chrome_options.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# time.sleep(2)

for i in range(50000):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    
    # instance of Options class allows
    # us to configure Headless Chrome
    options = Options()
    
    # this parameter tells Chrome that
    # it should be run without UI (Headless)
    options.headless = True
    
    # initializing webdriver for Chrome with our options
    driver = webdriver.Chrome(options=options)
    driver.get("https://this-person-does-not-exist.com/en")
    print(driver.title)

    # driver.set_window_size(1280, 1440)
    time.sleep(1)
    download_button = driver.find_element(By.XPATH, "//a[@id='download']")
    download_button.click()
    # time.sleep(1)
    # refresh_button = driver.find_element(By.XPATH, "//*[@id='reload-button']")
    # refresh_button.click()
    # time.sleep(4)


# for i in range(50000):
#     download_button = driver.find_element(By.XPATH, "//a[@id='download']")
#     download_button.click()
