# Implementation of Selenium WebDriver with Python using PyTest
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
DELAY = 3

test_users = [
    "SELENIUM_TEST",
    "Lois_Lane",
    "Clark_Kent",
    "Jenny_Flex",
]

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://rateer.pythonanywhere.com/')
    driver.maximize_window()
except Exception as e:
    print(str(e))
try:
    driver.find_element(by=By.XPATH, value='//a[@href="'+ "/home/signup/" +'"]').click()
    for i in test_users:
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "username" +'"]').send_keys(i)
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "email" +'"]').send_keys(i+"@seleniummail.com")
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "password" +'"]').send_keys(i)
        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()
        sleep(DELAY)
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}'\
            .format(
            'https://rateer.pythonanywhere.com/home/signup/',
            'Attempting to input',
            'Clicking submit'))
        try:
            ui_res = driver.find_element(by=By.XPATH, value='//h3[contains(text(), \'Registered Successfully!\')]').text
            print('\
            Then: Test Passed -- {}\n'\
            .format(
            ui_res))
        except Exception as e:
            print('\
            Then: Test Failed -- {}\n'\
            .format(
            str(e)))

    
    driver.find_element(by=By.XPATH, value='//a[@href="'+ "/home/" +'"]').click()

except Exception as e:
    print('\n\
        Feature: {}\n\
        Given conditions: {}\n\
        When: {}\n\
        Then: {}'\
        .format(
        'https://rateer.pythonanywhere.com/home/signup/',
        'Attempting to input',
        'Clicking submit',
        'Test Failed! Details:'+str(e)))
    print(str(e))
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)
    driver.quit()