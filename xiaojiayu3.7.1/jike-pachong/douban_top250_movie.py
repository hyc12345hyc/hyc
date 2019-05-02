import requests
import bs4
res = requests.get("https://movie.douban.com/top250")
soup = bs4.BeautifulSoup(res.text,"html.parser")
target = soup.find_all("div",class_="hd")
for each in target:
    print(each.a.span.text)