from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
JOBS_TO_SAVE = 3
PASS = "***************"


def login_linkedIn(driver):
    try:
        # Try to find the elements you need if not found raise exception
        mail = driver.find_element(By.CSS_SELECTOR, "#username")
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        login_btn = driver.find_element(
            By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    except:
        print("Due to some error we are unable to login")
        return False

    # If Sucess send information
    mail.send_keys(os.environ.get("GOOGLE_TEST_MAIL"))
    password.send_keys(PASS)
    login_btn.click()
    return True


def search_quries(driver, query):
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
    try:
        home = driver.current_url
        for num in range(JOBS_TO_SAVE):
            jobs = driver.find_elements(
                By.CSS_SELECTOR, ".entity-result__title-text")
            job = jobs[num]
            job.click()
            time.sleep(2)
            try:
                save_btn = driver.find_element(
                    By.CLASS_NAME, "jobs-save-button")
                save_btn.click()
                print("A job was saved")
            except:
                pass
            finally:
                driver.get(home)
                time.sleep(3)
        return True
    except NoSuchElementException:
        print("Jobs provided could not be saved")
        return False


def main():
    driver = webdriver.Chrome(service=service, options=option)
    cont_prog = True
    try:
        driver.get(url="https://www.linkedin.com/login")
    except:
        print("Unable visit URL")
        cont_prog = False

    if cont_prog:
        if login_linkedIn(driver):
            # Needed this in case of captcha
            time.sleep(8)
            global query
            if search_quries(driver, query):
                time.sleep(5)
                save_companies(driver)
    driver.quit()


if __name__ == "__main__":
    service = Service(executable_path="C:\Development\chromedriver.exe")
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    query = input("Enter the job you want to search for?")
    main()
