import requests
import bs4
import re

movies = []
ranks = []
messages = []
years = []

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

for x in range(0,2):
    res = requests.get("https://movie.douban.com/top250?start=%d" % (x*25),headers = head)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    movie = soup.find_all("div", class_="hd")
    rank = soup.find_all("span", property="v:average")
    message = soup.find_all("p",class_ ="")
    for each in movie:
        movies.append(each.a.span.text)
    for each in rank:
        ranks.append('评分：%s'%(each.text))
    for each in message:
        messages.append(each.text.replace(' ','').replace('\n',''))
        years.append(re.sub("\D", "", each.text.replace(' ', '').replace('\n', '')))
    result = []
    length = len(movies)
    for i in range (length):
        result.append([movies[i],ranks[i],messages[i],years[i]])
        result.append('\n')

with open('douban.txt', 'w',encoding="utf-8") as f:
    for each in (result):
        f.writelines(each)



