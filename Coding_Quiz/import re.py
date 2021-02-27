

# 정규표현식으로 원하는 문자열이나 키, 숫자 등을 조건에 맞추어서 사용하는 것이 가능함
# 정규표현식은 검색하면 많이 나오니 참고

#아래 코드는 a-zA-Z 정규 표현식을 이용해서 '124'라는 문자열에 알파벳이 들어가 있는지 판단하는 코드


import re
p = re.compile('[a-zA-Z]')
m = p.match( '124' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')