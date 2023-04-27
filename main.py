from bs4 import BeautifulSoup
from urllib.request import urlopen
import os.path

def remove_whitespace(text):
    text = "".join(line.strip() for line in text.split("\n"))
    return text

text_file = "tarnbyveien_nyheter.txt"

if os.path.isfile(text_file):
    with open(text_file, "r", encoding="utf-8") as file:
        old_text = file.read()
else:
    old_text = ""

url = "https://tarnbyveien.borettslag.net/nyheter/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


latest_news = soup.find("div", class_="mb-4")


# to make comparison easier
latest_news_edited = remove_whitespace(latest_news.get_text())
old_text_edited = remove_whitespace(old_text)

if old_text_edited != latest_news_edited:
    with open("tarnbyveien_nyheter.txt", "w", encoding='utf-8') as file:
        file.write(latest_news.get_text())