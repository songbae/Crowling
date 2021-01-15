import requests
from bs4 import BeautifulSoup
res= requests.get("https://app.sli.do/event/8tpauj7f/live/questions")
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select_one('div.app__content > div > sda-live > div > sda-questions > sda-question-list > div > div:nth-child(1) > div > div > div.question-item__body > span')
print(data)
# for i in data:
#     print(i.get_text())

