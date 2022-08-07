# Implementation of Selenium WebDriver with Python using PyTest
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_homepage_app():
   try:
      driver = webdriver.Chrome(ChromeDriverManager().install())
      driver.get('https://rateer.pythonanywhere.com/')
      driver.maximize_window()
   except Exception as e:
      print()

   title = "Rateer | HomePage"
   assert (title == driver.title),\
      '\n\
      Feature: {}\n\
       Given conditions: {}\n\
       When: {}\n\
       Then: {}'\
       .format('Attempting to open web page',
               'None',
               'Checking for title match',
               'Title doesnt match')


   print('\n\
      Feature: {}\n\
      Given conditions: {}\n\
      When: {}\n\
      Then: {}'\
      .format('Attempting to open web page',
      'None',
      'Checking for title match',
      'Test Passed!'))
   sleep(3)
   driver.quit()

test_homepage_app()
