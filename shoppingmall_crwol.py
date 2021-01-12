import requests
from bs4 import BeautifulSoup
# res= requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
# soup= BeautifulSoup(res.content,'html.parser')
# data=soup.select('#popular_srch_lst span a')
# for index,i in enumerate(data):
#     print(index+1,i.get_text())
# 쇼핑몰 크롤링 1
site_list=['https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000001','https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000']
# for site in site_list:
#     temp=requests.get(site)
#     res=BeautifulSoup(temp.content,'html.parser')
#     showim=res.select('#productListArea ul p')
#     print(site)
#     for index,i in enumerate(showim):
#         print(index+1, i.get_text())
# 여러 사이트들을 한번에크롤링 해보기 list형식으로 사이트 주소를 받아서 여러페이지를 순차적으로 크롤링할수있다.

# site='https://finance.naver.com/sise/'
# res= requests.get(site)
# soup= BeautifulSoup(res.content, 'html.parser')
# data1= soup.select('#popularItemList>li')
# for index, i in enumerate(data1):
#     print(i.find('a').get_text())
# 주식사이트 크롤링

# urllib 사용법
# request와 urlib의 차이점은
from urllib.request import urlopen
# res= urlopen('')
# soup=BeautifulSoup (res,'html.parser)
# 기존의 request는 res.content 라는곳에 리턴값이 들어간데 반해 urllib는 res자체가 리턴값이다.


#여러 페이지를 한번에 크롤링 하는법 !
#http 규격에 따라서 200일경우 정상 응답이지만 그외에는 오류(대부분 페이지가없을때)
# 따라서 확인을 해야한다.
#페이지 오류 확인법
 # if res.staus_code !=200:
 #     print('페이지없음')
 # else :
 #     soup=BeautifulSoup(res.content,'html.parser')
 #     data=soup.select('h4.card-text')
 #     for item in data:
 #         print(item.get_text())

# 여러개를 어떻게 하나 했더니 별거 없다 정석적인 방법이라기보다는 그냥
# 페이지 주소에 뒤에 숫자를 하나씩 추가해가면서 포문 돌리는게 끝이다
# 이런 방법말고 정확한 방법을 원한다.

# res= requests.get('https://www.acmicpc.net/group/workbook/view/8918/29115')
# if res!=200:
#     print('접속불가')
# else:
#     prrint('접속가능')
# soup= BeautifulSoup(res.content,'html.parser')
# data= soup.select('#table_body tr')
# for i in data:
#     print(i.get_text())

session = requests.session()
url='https://www.acmicpc.net/signin'

data={
    'login_user_id': 'ilbul2',
    'login_password': 'pk@5770114',
    'next': '/',
    'stack': '0',
    'g-recaptcha-response': '03AGdBq27MNqKPwhIdYANQ1B3hGxqXxBSocc9XoLo5fhAvGYOsMCVVb-jew7Ff0rw61IVZqpnArVbX7AUFcnapa83AMOom_b9suxIU5DtewRM0cFsHs5f-J_zqVDU2WU6GmuGtllP_mUzMi7avMjv6LbRBr74YvejXQSK5o5gzw91V3ES1a2hd3hokoQKgYbu44cuZ03bU3MgH3G8Cqu9WOiLzkzmZmhLK5cSuOmuaUiFBCcl6PJD2uBzgBW18CcfmYTnEGhvnbk66FXx2AehFAjCTv8GZdc8gTR2OXH6jUvLyGcoX_JWp7GpohcpVcnkGo72LogPbyVUmwHIK01z9_mLjZ84YJadKPcF15RDOcD00U97O8pp-7YSnC2sweKl2M86ZfLXX8HxnzkajPkdMHoc9fSPtLfsEbbk04VCs41BmdX4_UG97wybFKbUqLenNameNIe5N0_2Q'
}
response=session.post(url,data=data)
#로그인 실행
response.raise_for_status()
url='https://www.acmicpc.net/group/workbook/view/8918/29115'
res=response.get(url)
print(res)
soup=BeautifulSoup(res.content,'html.parser')
print(soup)
data=soup.select('#table_body > tr:nth-child(1) > td:nth-child(1)')
for i in data:
    print(i.get_text())


