import requests
import bs4

comments = []

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}

res = requests.get("https://music.163.com/#/song?id=4466775" ,headers = head)
soup = bs4.BeautifulSoup(res.text, "html.parser")
comment = soup.find_all("a" , class_="s-fc7")
for each in comment:
    comments.append(each.text)

print(comments)