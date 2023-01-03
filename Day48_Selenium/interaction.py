from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os
service = Service(executable_path="C:\Development\chromedriver")
mail = os.environ.get("GOOGLE_TEST_MAIL")

with webdriver.Chrome(service=service) as driver:
    driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-150747833%3A1672731727150853&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh42--o8WKgM1bO2_uD2W0w_VlXgmPRY5OTiAayEPigsRY2AvRd1NbFWtEs_MIOzP9E1T3-R")
    email = driver.find_element(By.ID, 'identifierId')
    email.send_keys(mail)
    email.send_keys(Keys.ENTER)

    # password.send_keys(os.environ.get("GOOGLE_TEST_PASSWORD"))


# with webdriver.Chrome(service=service) as driver:
#     driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
#     search = driver.find_element(By.NAME, "search")
#     search.send_keys("Python")
#     search.send_keys(Keys.ENTER)


# with webdriver.Firefox() as d1:
#     d1.get(url="https://en.wikipedia.org/wiki/Main_Page")
#     ele = d1.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#     print(ele.get_attribute("textContent"))
