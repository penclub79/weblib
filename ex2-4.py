#http.client.HttpConnection GET 방식 요청   (저수준)다른방식이다

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')    #도메인만 적어준다.
conn.request('GET', '/')

result = conn.getresponse()
# print(result)
print(result.status, result.reason)
#여기까지 헤더부분을 읽어왓다

# data = result.read()
# print(data)
# result = conn.request('GET', '/hello.html')
# print(result)

# GET, POST, [PUT, DELETE, HEAD]  []=은 많이 안쓴다.
