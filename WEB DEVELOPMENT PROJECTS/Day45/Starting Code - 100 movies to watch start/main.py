import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

#get the html contents of the url
response = requests.get(URL).text

#pass the contents to beautisoup
soup = BeautifulSoup(response, "html.parser")

#get the h3 inside a div with class="title"
class_title = soup.select("div h3")

with open("WEB DEVELOPMENT PROJECTS/Day45/Starting Code - 100 movies to watch start/movies.txt", mode="w", encoding="utf-8") as file:
    #get each texts in reverse
    for title in class_title[::-1]:
        file.write(f"{title.text}\n") 


