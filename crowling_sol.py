from bs4 import BeautifulSoup
import requests
res= requests.get('http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06')
soup= BeautifulSoup(res.content,'html.parser')
bestlist=soup.select('div.best-list')
bestitems=bestlist[1]
products= bestitems.select('ul>li')
for index,product in enumerate(products):
    title=product.select_one('a.itemname')
    price=product.select_one('div.s-price>strong')

    res_info=requests.get(title['href'])
    soup_info= BeautifulSoup(res_info.content,'html.parser')
    provider_info=soup_info.select_one('div.item-topinfo > div.item-topinfo_headline > p > a > strong')
    print(index+1,title.get_text(),price.get_text(),provider_info.get_text())