# Twitter Bot - Unable to pass authentication tests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome(service=service, options=option)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.browser.get(url="https://www.speedtest.net/")
        start_test = self.browser.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_test.click()
        time.sleep(40)
        # Getting download(self.down) and upload(self.up)
        down_speed = self.browser.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = float(down_speed.get_attribute("textContent"))

        up_speed = self.browser.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = float(up_speed.get_attribute("textContent"))

        print(f"Upload speed :{self.up}\nDownload speed :{self.down}")
        # self.browser.quit()

    def tweet_at_provider(self):
        msg = f'Internet speed is okay I guess. Upload - {self.up}, Download - {self.down}'
        tweet = self.browser.find_element(
            By.CSS_SELECTOR, '.notranslate .public-DraftEditor-content')
        tweet.send_keys(msg)
        tweet_send = self.browser.find_element(
            By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_send.click()
        self.browser.quit()

    # Not able to log in
    def twitter_login(self):
        self.browser.get("https://twitter.com/login?lang=en")
        print("sleeping")
        time.sleep(60)
        print("wokeup")


def main():
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    # bot.twitter_login()
    # bot.tweet_at_provider()


if __name__ == "__main__":
    service = Service(executable_path="C:\Development\chromedriver.exe")
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    main()
