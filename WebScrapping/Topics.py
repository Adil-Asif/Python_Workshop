#Beautiful Soup Documentation Link
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
import bs4
res=requests.get('https://en.wikipedia.org/wiki/Web_scraping')
#print(res.text)
#print(type(res))
soup=bs4.BeautifulSoup(res.text,'lxml')
#print(soup)
#soup.select('.toctext')
for i in soup.select('.toctext'):
   print(i.text)