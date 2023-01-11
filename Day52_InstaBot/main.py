from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time


class Instafollower:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome(service=service, options=option)

    def login(self):
        self.browser.get(url=URL)
        self.browser.maximize_window()
        time.sleep(3)
        mail = self.browser.find_element(By.NAME, 'username')
        print(mail.get_attribute("textContent"))
        mail.send_keys(os.environ.get("GOOGLE_TEST_MAIL"))
        password = self.browser.find_element(By.NAME, 'password')
        password.send_keys(INSTA_PASS)
        btn = self.browser.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        btn.click()
        time.sleep(3)

    def find_followers(self):
        try:
            search_icon = self.browser.find_element(
                By.XPATH, "//div[text()='Search']")
        except:
            print('Unable to parse search bar')
            return False

        search_icon.click()
        time.sleep(2)
        query = self.browser.find_element(
            By.TAG_NAME, 'input')
        query.send_keys('ChefSteps')
        time.sleep(3)
        query.send_keys(Keys.ENTER)
        query.send_keys(Keys.ENTER)
        time.sleep(3)
        return True

    def follow(self):
        self.browser.find_element(
            By.XPATH, "//div[text()=' followers']").click()
        time.sleep(3)
        followers = self.browser.find_elements(
            By.XPATH, "//div[text()='Follow']")
        for person in followers[:5]:
            person.click()


def main():
    bot = Instafollower()
    bot.login()
    if bot.find_followers():
        bot.follow()
    else:
        print("Could not find the given result")


if __name__ == '__main__':
    URL = "https://www.instagram.com/"
    INSTA_PASS = "Your insta password"
    service = Service(executable_path="C:\Development\chromedriver.exe")
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    main()
