from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script ends

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)

# Open the Amazon website
driver.get('https://www.python.org/')

time_event = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul')
new_list = []
for i in time_event:
   new_list += i.text.split("\n")

time_event_dict = {}

for i in range(len(new_list)):
    if i%2 == 0:
        time_event_dict[f"{int(i - (i/2))}"] = {"time": new_list[i], "name": new_list[i+1]}


print(time_event_dict)
driver.quit()
