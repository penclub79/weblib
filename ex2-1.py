#urlparse

from urllib.parse import urlparse, urlsplit, urljoin, parse_qs

url = "http://www.python.org:80/guido/python.html;philosophy?a=10&b=20#here"  #url자원
                            #philosophy?a=10#here 잘안쓰는 문법
                            #a=10은 파라미터
result = urlparse(url)
print(url)