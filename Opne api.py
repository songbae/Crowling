import requests
client_id='jmQb2PtWLj3xrNO4tW52'
client_pw='7XNZlUazo2'

naver_open_api='https://openapi.naver.com/v1/search/news.json?query=android'

header_param={"X-Naver-Client-Id":client_id,"X-Naver-Client-Secret":client_pw}
res= requests.get(naver_open_api,headers=header_param)
if res.status_code !=200:
    print('아니야')
else:
    data=res.json()

for idx,item in enumerate(data['items']):
    print(idx+1,item['title'],item['link'])
#요청 변수명 query, display, start ,sort 등이 있다
# quert는 검색을 원하는 문자열로서 UTF-8로 인코딩한다.
# distplay는 integer 타입으로 검색 결과 건수 지정 (기본값10, 최대100)
# start 는 integer 타입으로 기본값(1, max=1000) 검색시작 위치로 최대 1000까지가능
# sort는 string 타입으로 sim(기본값), data, asc, dsc 정렬옵셥을 줄 수있다.
#  기본값은 유사도 순 date는 최신순 , 가격 오름차순, 가격 내림차순.
