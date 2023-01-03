from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\Development\chromedriver")

# Initialise the web driver
with webdriver.Chrome(service=service) as driver:
    # navigating to the url
    driver.get("https://www.amazon.in/gp/product/B09WY78WLX/ref=s9_acss_bw_cg_Header_5c1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=0W3TT9DY613AFMN2AQDX&pf_rd_t=101&pf_rd_p=2f8e9ea1-1a13-4d69-b510-a5a06b05c603&pf_rd_i=1375424031&th=1")
    # find element by css selector
    # sol = driver.find_element(by=By.CSS_SELECTOR, value="span.a-price-whole")
    # price = "".join(sol.get_attribute("textContent").split('.')[0].split(','))
    # print(price)

    soln = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[32]/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/table/tbody/tr[3]/th')
    print(soln.get_attribute("textContent"))
