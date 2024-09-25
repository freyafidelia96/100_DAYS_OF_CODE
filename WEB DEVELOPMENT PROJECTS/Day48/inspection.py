from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script ends

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open the Amazon website
driver.get('https://secure-retreat-92358.herokuapp.com/')

fName = driver.find_element(By.NAME, value="fName")
lName = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, value=".btn-lg")

fName.send_keys("Fidelia")
lName.send_keys("Achi")
email.send_keys("freyafidelia@gmail.com")
button.click()



