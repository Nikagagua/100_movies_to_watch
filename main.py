import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
arch_web_page = response.text

soup = BeautifulSoup(arch_web_page, "html.parser")
all_movies = soup.find_all(name='h3', class_='title')
movie_titles = [movie.getText() for movie in all_movies]
top_100_movie = movie_titles[::-1]

with open('movies.txt', 'w', encoding='utf-8') as movies:
    for movie in top_100_movie:
        movies.write(f"{movie}\n")
