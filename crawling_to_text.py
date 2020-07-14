from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen(('http://www.cgv.co.kr/movies/'))
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("cgv_movie_rank.txt", 'w')
for anchor in soup.select("strong.title"):
    data = str(i) + "À§ : " + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()