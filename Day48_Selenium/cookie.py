from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# set unit of time in minutes
TIME = 1
service = Service(executable_path="C:\Development\chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=option)

driver.get(url="https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
lang_select = driver.find_element(By.ID, "langSelect-EN")
lang_select.click()
time.sleep(5)
cookie = driver.find_element(By.ID, "bigCookie")

timeout = time.time()+10
five_min = time.time()+60*TIME


while True:
    cookie.click()
    if time.time() > timeout:
        num = 0
        # clicking on upgrades
        try:
            while num <= 7:
                upgrade = driver.find_element(
                    By.CSS_SELECTOR, f"#upgrade{num}")
                while 'enabled' in upgrade.get_attribute('class'):
                    upgrade.click()
                num -= 1
        except:
            pass
        num = 18
        # purchasing the products
        while num >= 0:
            product = driver.find_element(By.CSS_SELECTOR, f'#product{num}')
            # print(product.get_attribute("class"))
            while 'enabled' in product.get_attribute("class"):
                # print('should have clicked')
                product.click()
            num -= 1
        timeout = time.time()+10

    if time.time() > five_min:
        try:
            cookies_per = driver.find_element(
                By.CSS_SELECTOR, '#cookiesPerSecond')
            print("\nshould print cookies per second\n")
            print(cookies_per.get_attribute('textContent'))
            break
        except:
            print("\n\n\nexception occured during end")
            break

driver.close()
