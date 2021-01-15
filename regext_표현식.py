import re

pattern=re.compile('D*A')
pattern.search("A")
pattern.search("DA")
print(pattern.search("DDDDDDDDDDDDDA"))

#또다른 반복 표현 :{n},{m,n}
# {n}앞문자가 n번 반복되는 표현
# {m,n} 앞문자가 m번 반복되는 패턴부터 n번 반복되는 패턴까지

# []괄호 : 괄호 안에 들어가는 문자가 들어있는 패턴
# [abc]는 a,b,c중 하나가 들어있는 패턴을 말함
#[a-zA-Z]이럴경우 대소문자 모두를 가져올수있다
#[a-zA-Z0-9]로 표기 할시 대소문자를 모두 포함해서 앞파벳 전체를 가져올수있다.

# findall 함수: 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 리턴함
pattern =re.compile('[a-z]+')
FD= pattern.findall('Game of Life in python')
print(FD)

#split함수  : 찾은 정규표현식 패턴 문자열을 기준으로 문자열을 분리

pattern2=re.compile(':')
ans= pattern2.split('pathon:jave')
print(ans)
#sub 함수: 찾은 정규표현식 패턴 문자열을 다른 문자열로 변경
pattern=re.compile('-')
subed= patter.sub('*','8080080-80090')
#-> 이럴경우 기존의 - -> *으로 변경 된다

# 예시: 데이터에서 정규식 사용하기
res= urlopen('')
soup= BeautifulSoup(res,'html.parser')
data=soup.select('ul#dev_course_list li.course')
for item in data:
    print(re.sub('\[[0-9]+\]'),item.get_text())
