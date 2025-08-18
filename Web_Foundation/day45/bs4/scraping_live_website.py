import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.select_one("span.titleline a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for artticle_tag in articles:
    text = artticle_tag.find("a").getText()
    article_texts.append(text)
    link = artticle_tag.find("a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

print(article_texts)
print(article_links)
print(article_upvotes)
