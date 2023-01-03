import smtplib
import os
import requests
import lxml
from bs4 import BeautifulSoup

MONEY_ALLOTTED = 210400
URL = "https://www.amazon.in/gp/product/B09WY78WLX/ref=s9_acss_bw_cg_Header_5c1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=0W3TT9DY613AFMN2AQDX&pf_rd_t=101&pf_rd_p=2f8e9ea1-1a13-4d69-b510-a5a06b05c603&pf_rd_i=1375424031&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept-Language": "en-US,en;q=0.5"
}


def send_mail(price):
    MY_MAIL = os.environ.get("GOOGLE_TEST_MAIL")
    PASSWORD = os.environ.get("GOOGLE_TEST_PASSWORD")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        msg = f'''Subject:Best Deal
        

        Dell Alienware x14 Gaming Laptop, Intel i7-12700H, 14 inches(35.5cm) FHD 144Hz 400nits GSYNC+ Advanced Optimus,
        32GB DDR5, 1TB SSD, Nvidia RTX 3060 6GB, Dolby Atmos, Lunar Light (1.84 kgs) D569939WIN9 just at Rs {price}
        
        Go get it: {URL}'''
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs="testingpython63@yahoo.com",
            msg=msg)


def main():
    content = requests.get(url=URL, headers=header)
    website_text = content.text

    soup = BeautifulSoup(website_text, "lxml")
    price_data = soup.find(name="span", class_="a-price-whole").getText()
    price_int, _ = map(str, price_data.split('.'))
    price = float("".join(price_int.split(",")))
    if price < MONEY_ALLOTTED:
        send_mail(price)


if __name__ == "__main__":
    main()
