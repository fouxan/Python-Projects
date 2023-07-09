from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

soup = BeautifulSoup(response, "html.parser")
data = soup.find_all(name="h3", class_="title")
names = [tag.getText() for tag in data]

movies = names[::-1]

with open("Top 100 movies.txt", "w") as f:
    for movie in movies:
        f.write(movie + "\n")