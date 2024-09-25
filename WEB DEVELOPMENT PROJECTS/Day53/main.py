from selenium import webdriver
from selenium.webdriver.common.by import By


URL = 'https://appbrewery.github.io/Zillow-Clone/'

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script ends

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get(URL)

links = driver.find_elements(By.CSS_SELECTOR, value='.property-card-link')
addresses = driver.find_elements(By.CSS_SELECTOR, value='.Image-c11n-8-84-listing')
prices = driver.find_elements(By.CSS_SELECTOR, value='.PropertyCardWrapper__StyledPriceLine')

links_list = []
addresses_list = []
price_list = []


for i in range(len(links)):
    links_list.append(links[i].get_attribute('href'))
    addresses_list.append(addresses[i].get_attribute('alt'))
    price_list.append(prices[i].text.split('+')[0] if '+' in prices[i].text else prices[i].text.split('/')[0])


print(f'{links_list}\n')
print(f'{addresses_list}\n')
print(price_list)



driver.quit()