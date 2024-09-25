from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script ends

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open the Amazon website
driver.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

path = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[9]/div[5]/div[4]/div[1]/div/h1/span')
print(path)
print(f"price is {price_dollar.text}.{price_fraction.text}")

driver.quit()
