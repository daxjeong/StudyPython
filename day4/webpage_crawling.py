# 웹페이지 긁어오기
# 웹 : request에 대한 respond
from urllib.request import Request, urlopen
# # import 패키지명.하위 패키지명
# # 모듈은 누군가 만들어놓은 파이썬 파일(.py), 이를 모아둔 폴더를 패키지

req = Request('https://www.naver.com') # 네이버 웹페이지 요청
res = urlopen(req)
print(res.status)

# 202 : page found
# 404 : not found

# 외부 request 패키지 추가 설치
# pip install requests
import requests
url = 'https://www.naver.com'
res = requests.get(url)

# print(res.status_code)
print(res.text)