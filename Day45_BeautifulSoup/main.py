from bs4 import BeautifulSoup
import lxml
# use lxml parser if html.parser is not working
# with open("Day45_BeautifulSoup/website.html", mode="r", encoding="utf-8") as fs:
#     contents = fs.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.p)  # first <p> tag
# anchor_tags = soup.find_all(name="a")  # It's a list
# print(anchor_tags[0]['href'])

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# # selecting using css selectors
# ####################################
# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.find(name="a").text
    article_texts.append(article_text)
    article_link = article_tag.find(name="a").get('href')
    article_links.append(article_link)

scores = [int(score.getText().split()[0])
          for score in soup.select(selector=".score")]

indx = scores.index(max(scores))

print(article_links[indx])
print(article_texts[indx])
print(scores[indx])
