#http.client.HttpConnection GET 방식 요청   (저수준)다른방식이다
from html.parser import HTMLParser  #파싱하기위함
from http.client import HTTPConnection


conn = HTTPConnection('www.example.com')    #도메인만 적어준다.
conn.request('HEAD', '/')   #HEAD만 보내기 헤드명령은 많이 쓰지않음

result = conn.getresponse()
print(result)
# print(result.status, result.reason)

data = result.read()
print(data)

