from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import random

from selenium import webdriver
from fake_useragent import UserAgent


time.sleep(random.uniform(0.5, 2.5))


ua = UserAgent()
user_agent = ua.random


# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script ends

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)
time.sleep(random.uniform(0.5, 2.5))

# Open the Amazon website
driver.get('https://www.linkedin.com/')

sign_in = driver.find_element(By.XPATH, value='/html/body/nav/div/a[2]')
time.sleep(random.uniform(0.5, 2.5))

sign_in.click()

email_info = driver.find_element(By.ID, value='username')
password = driver.find_element(By.ID, value='password')

time.sleep(random.uniform(0.5, 2.5))

email_info.send_keys("fidelia.100daysofcode@gmail.com")
password.send_keys("byyourspirit")

send = driver.find_element(By.CSS_SELECTOR, value='.from__button--floating')
time.sleep(random.uniform(0.5, 2.5))

send.click()

# jobs_icon = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
# jobs_icon.click()

search_box = driver.find_element(By.CSS_SELECTOR, '.search-global-typeahead__input ')
time.sleep(random.uniform(0.5, 2.5))

# Send keys to the search box
search_box.send_keys("Python Developer")
search_box.click()

time.sleep(random.uniform(0.5, 2.5))


search_box_click = driver.find_element(By.CSS_SELECTOR, '.search-global-typeahead__collapsed-search-button')
search_box_click.click()

