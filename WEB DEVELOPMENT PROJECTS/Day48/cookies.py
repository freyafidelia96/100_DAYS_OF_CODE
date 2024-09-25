from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script ends

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open the Amazon website
driver.get('https://orteil.dashnet.org/cookieclicker/')

# Wait until the "English" div element is clickable
english_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)

english_button.click()

big_cookie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div button"))
)

duration = 300

start_time = time.time()

while (time.time() - start_time) < duration:
    elasped_time = round(time.time() - start_time)
    run = elasped_time % 5 == 0
    big_cookie.click()
    if run:
        for i in range(4, 0, -1):
            try:
                textNo_cookies = driver.find_element(By.ID, value="cookies")
                noOf_cookies = int(textNo_cookies.text.split(" ")[0])

                product_price = driver.find_element(By.XPATH, value=f'//*[@id="productPrice{i}"]')
                product_price = int(product_price.text)

                if noOf_cookies >= product_price:
                    buy_upgrade = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="product{i}"]')))
                    buy_upgrade.click()

            except Exception:
                continue

textNo_cookies = driver.find_element(By.ID, value="cookies")
print(textNo_cookies.text)

driver.quit()
