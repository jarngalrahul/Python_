from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os


def login_linkedIn(driver):
    try:
        mail = driver.find_element(By.CSS_SELECTOR, "#username")
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        login_btn = driver.find_element(
            By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    except:
        print("Due to some error we are unable to login")
        return False
    finally:
        mail.send_keys(os.environ.get("GOOGLE_TEST_MAIL"))
        password.send_keys("-------------")
        login_btn.click()
        return True


# still not working do it tommorow
def search_quries(driver, query):
    print(query)
    try:
        search = driver.find_element(
            By.XPATH, '//*[@id="global-nav-typeahead"]/input')
        search.send_keys(query)
        search.send_keys(Keys.ENTER)
    except:
        print("Companies could not be found")
        return False
    return True


def save_companies(driver):
    print("Saving companies")
    try:
        jobs = driver.find_elements(By.CLASS_NAME, "app-aware-link")
        for job in jobs:
            job.click()
            save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
            save_btn.click()
        return True
    except:
        print("Companies could not be saved")
        return False


def main():
    service = Service(executable_path="C:\Development\chromedriver.exe")
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=option)
    cont_prog = True
    try:
        driver.get(url="https://www.linkedin.com/login")
    except:
        print("Unable visit URL")
        cont_prog = False

    if cont_prog:
        if login_linkedIn(driver):
            global query
            if search_quries(driver, query):
                time.sleep(5)
                save_companies(driver)


if __name__ == "__main__":
    query = input("Enter the job you want to search for?")
    main()
