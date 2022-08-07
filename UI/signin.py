from curses.ascii import DEL
from unittest import FunctionTestCase
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
test_users = [
    "SELENIUM_TEST",
    "Lois_Lane",
    "Clark_Kent",
    "Jenny_Flex",
]
DELAY = 3

def signin(driver, username, password):
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+ "/home/signin/" +'"]').click()
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "username" +'"]').send_keys(username)
        driver.find_element(by=By.XPATH, value='//input[@name="'+ "password" +'"]').send_keys(password)
        driver.find_element(by=By.XPATH, value='//button[@type="'+ "submit" +'"]').submit()
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}'\
            .format(
            'https://rateer.pythonanywhere.com/home/signin/',
            'Attempting to input',
            'Clicking submit',
            'Test Passed!'))
    except Exception as e:
        print('\n\n\
            Feature: {}\n\
            Given conditions: {}\n\
            When: {}\n\
            Then: {}'\
            .format(
            'https://rateer.pythonanywhere.com/home/signin/',
            'Attempting to input',
            'Clicking submit',
            'Test Failed! Details:'+str(e)))

if __name__ == '__main__':
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://rateer.pythonanywhere.com/')
        driver.maximize_window()
    except Exception as e:
        print(str(e))
        exit(1)

    print("Starting test [Sign In]")
    signin(driver, test_users[0], test_users[0])
    print("Finished test [Sign In]")
    sleep(DELAY)
    sleep(DELAY)
    sleep(DELAY)  