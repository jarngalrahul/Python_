from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLScOkQbo9fi5ea9ib2Pfs5BrLh8oGKvTnnGk3ekrVkTM0cxR0Q/viewform?usp=sf_link'


class GoogleForms:
    def __init__(self) -> None:
        self.driver = self.create_driver()

    def max_screen(self):
        self.driver.maximize_window()

    def create_driver(self):
        service = Service(executable_path='C:\Development\chromedriver.exe')
        option = webdriver.ChromeOptions()
        option.add_experimental_option('detach', True)
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        return webdriver.Chrome(service=service, options=option)

    def update_google_form(self, property_data: dict):
        for key in property_data:
            self.driver.get(url=FORM_LINK)
            time.sleep(2)
            addr = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            addr.send_keys(property_data[key]['address'])

            price = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price.send_keys(property_data[key]['rent_price'])

            lnk = self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            lnk.send_keys(property_data[key]['link_to_property'])

            self.driver.find_element(
                By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
        self.driver.quit()
