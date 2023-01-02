from bs4 import BeautifulSoup
import requests

content = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = content.text

soup = BeautifulSoup(web_page, "html.parser")

headings = soup.find_all(name="h3", class_="title")

# for title in headings[::-1]:
# print(title.getText())

# OR

for title in reversed(headings):
    print(title.getText())
