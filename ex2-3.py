#POST 방식으로 웹 서버에 요청 보내기(url오픈햇음)
from urllib.request import urlopen, Request
from urllib.parse import urlencode

data = urlencode({'a' : 10, 'b': 20, 'name':'둘리'})
# data = 'a=10&b=20&name=둘리' 스트링으로 하나로 다주엇을때 encoding을 해야함
data = data.encode('UTF-8') #바이트 코드로 만들어야하기때문에 해야한다.
print(data)

request = Request('http://www.example.com', data)
# print(request)
#Request 객체를 사용한 request 헤더 변경  리퀘스트를 쓰는 이유이다.
request.add_header('Content-Type', 'text/html')
# print(request)
f = urlopen(request)
print(f.read())
