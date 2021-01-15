# 문자열에 있는 특성 문자 갯수 세기
string = 'David Id is '
string.index('D')
# 문자열의 인덱스 반환
string.find('Dav')
# 똑같이 index를 반환하지만 없을경우 return -1 을 한다
string ='12345'
comma =','
comma.join(string)
# 이경우 껴넣을 문자.join(문자열) 문자열 사이에 껴넣을 수있다.
data = ' d ace'
data.strip()
## 앞뒤 공백을 다지운다.
# lstrip() 왼쪽 공백 지운다 rstrip() 오른쪽 공백 지우기
string= "    99999 (dave)8888"
string,strip("98()")
# 이럴경우 9,8,(,) 이 문자를 모두 지운다 default 값이 공백을 지우는것일뿐!
string.upper()
string.lower()
## 대문자 소문자로 치환
# 정규표현식
import re
string ="(dave)"
re.sub('[^a-zA-Z0-9]','',string)# 정규식, 대체, 값