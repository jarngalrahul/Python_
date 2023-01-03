from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Development\chromedriver")

with webdriver.Chrome(service=service) as driver:
    driver.get(url="https://www.python.org/")
    dict_ = {}
    upcoming_events = driver.find_elements(
        By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
    for num in range(len(upcoming_events)):
        date_name = upcoming_events[num].get_attribute(
            "textContent").split('\n')
        dict_[num] = {"time": date_name[1], "name": date_name[2].strip()}
    print(dict_)
