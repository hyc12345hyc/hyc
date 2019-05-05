import requests
import bs4
import openpyxl
a = []
for x in range(0,3):
    res = requests.get("https://movie.douban.com/top250?start=%d" % (x*25))
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    target = soup.find_all("div", class_="hd")
    for each in target:
        with open('douban.txt', 'w') as f:
            a.append(each.a.span.text)
            a.append('\n')
            f.writelines(a)


