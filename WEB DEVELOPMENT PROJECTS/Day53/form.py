from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from main import links_list, addresses_list, price_list


# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open after the script ends

# Initialize the Chrome driver with the options
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSe5jVVbzwM-1i3OVtwj1IPEEYB775EFXufUQPzkddE9uHwFnA/viewform?usp=sf_link')

for i in range(len(links_list)):
    short_answers = driver.find_elements(By.CSS_SELECTOR, value='.zHQkBf')
    for j in range(len(short_answers)):
        print(type(short_answers[j]))
        if j == 0:
            short_answers[j].send_keys(f'{addresses_list[i]}')
        elif j == 1:
            short_answers[j].send_keys(f'{price_list[i]}')
        else:
            short_answers[j].send_keys(f'{links_list[i]}')

    button = driver.find_element(By.CSS_SELECTOR, value='.RveJvd')
    button.click()

    go_back = driver.find_element(By.TAG_NAME, value='a')
    go_back.click()


driver.quit()
