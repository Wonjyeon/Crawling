from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen(('https://movie.naver.com/movie/sdb/rank/rmovie.nhn'))
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("���̹�_��ȭ����.txt", 'w')
for anchor in soup.select("div.tit3 > a"):
    print(str(i) + "�� : " + anchor.get('title', '/'))
    i = i + 1