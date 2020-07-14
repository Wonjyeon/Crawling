from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen(('https://movie.naver.com/movie/sdb/rank/rmovie.nhn'))
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("네이버_영화순위.txt", 'w')
for anchor in soup.select("div.tit3 > a"):
    print(str(i) + "위 : " + anchor.get('title', '/'))
    i = i + 1