import requests
import bs4
import re

years = []
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

for x in range(0,2):
    res = requests.get("https://movie.douban.com/top250?start=%d" % (x*25),headers = head)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    movie = soup.find_all("div", class_="hd")
    rank = soup.find_all("span", property="v:average")
    message = soup.find_all("p",class_ ="")
    for each in message:
        years.append(re.sub("\d", "", each.text.replace(' ', '').replace('\n', '')))
        result = []
        length = len(years)
        for i in range(length):
            result.append([years[i]])
            result.append('\n')

    with open('douban.txt', 'w', encoding="utf-8") as f:
        for each in (result):
            f.writelines(each)