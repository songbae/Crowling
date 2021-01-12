import requests
from bs4 import BeautifulSoup
res= requests.get("http://v.media.daum.net/v/20170615203441266")
soup = BeautifulSoup(res.content, 'html.parser')
mydata =soup.find('h3', 'tit_view')
data1=soup.find('div', 'layer_util layer_summary')
print(data1.get_text())

print(mydata.string)

# 마크업 언어: 문서나 데이터의 구조
# 태그로 검색 방법
#
html=""
soup = BeautifulSoup(html, "html.parser")
# 태그로 검색방법
data = soup.find('p', attrs={'class':'cssstyle'})# 이런식으로 속성값 자체를 넣어서 만들수도 있다.
data = soup.find_all('p') # 이런식으로 모든 p태그를 뽑아올수 있는데 이때는 리스트 형식으로 만들어지기 때문에 for 문을 이용해서 출려할수있다.
# css언어란 ?
# style 속성으로 태그에 넣기
# <td style = "text-align:center ; color:blue">
#              텍스트어라인 -> 프로퍼티 와 center->값 을 연속해서 사용 가능 띄어쓰지 않아도 되고 ,띄어도됨
#text-align 어떤식으로 정렬할것인지  left center right 으로 쓸수있음 보통 프로퍼티 와 값으로 나타낸다.

# css언어 적용하기
# 적용할 태그에 style 속성을 넣기
# html문서 <head>안에 <style>태그로 넣기
# html문서 <head>안에 css파일로 링크하기

# 크롤링 패턴 코드
# 크롤링 후처리
# /n 불필요한 데이터 처리하기 


res= requests.get('http://v.media.daum.net/v/20170615203441266')
soup= BeautifulSoup(res.content,'html.parser')
data= soup.find('title')
print(data.get_text())

# 크롤링 팁1 -크롬 브라우저 활용하기
# 오픈 크롬 브라우저
# 오픈 크롬 개발자 모드
result = requests.get('http://davelee-fun.github.io/blog/crawl_test')
soup1=BeautifulSoup(result.content, 'html.parser')
section = soup1.find('ul', id='dev_course_list')
titles= section.find_all('li','course')
for i in titles:
    print(i.get_text())
for i in titles:
    print(i.get_text().split('[')[0].split('-')[1].strip())
# 팁2 추출한 것에서 또 추출하기
# split을 이용한 전처리 하기
#strip 을 이용한 전처리 하기

#CSS Selector 사용법
#- select()안에 태그 또는 CSS class이름등을 넣어주면됨
#- 결과값은 리스트 형태로 반환됨
# 매칭 되는 첫번째 데이터만 얻고자 할때는 select_one()을 사용한다.

soup= BeautifulSoup(res.content,'html.parser')
items=soup.select('li a')
for i in items:
    print(i.get_text())
# select 문에서 space를 사용할 경우 그안 어딘가에 하위 단어가 class가 있다는것이고
# > 꺽쇠를 이용할 경우 바로 밑에 존재한다는것을 나타낸다.
items=soup.select('ul#dev_course_list >li.course.paid')
# 위에 문법같은경우 id=#으로 대체 해서 쓸수 있고 dev_course_list 클래스 바로 밑에
# li.course.paid라는 연결된 상태가 있을때 쓸수있따.
