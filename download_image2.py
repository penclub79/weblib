from html.parser import HTMLParser
from http.client import HTTPConnection
from urllib.request import urlopen, Request
from urllib.parse import urlencode

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):  #함수를 호출하면서 파싱된다 tag하고 attribute해주고
        # print(tag)
        if tag != 'img':
            return
        # print(tag, attrs)
        if not hasattr(self, 'result'):  #this랑 비슷한거
            self.result = []
        for name, value in attrs:
            if name == 'src':
                # print(value)
                self.result.append(value)


def main():
    conn = HTTPConnection('localhost:9999')

    conn.request('GET', '/graph')
    r = conn.getresponse()
    print(r.status, r.reason)

    data = r.read()

    # conn.request('GET', '/graph')
    # r = conn.getresponse()
    # print(r.status, r.reason)

    # conn = HTTPConnection("localhost:9999")
    # # print(conn)
    #
    # params = urlencode({'ex': 2})
    # # print(params)
    # headers = {"Content-type": "localhost:9999",
    #            "Accept": "text/html"}
    # print(headers)
    # conn.request("POST", "/graph", params, headers)
    # response = conn.getresponse().headers.get_content_charset()
    # print(response.status, response.reason)
    #
    # data = response.read().decode(response)
    # print(data)



if __name__ == '__main__':
    main()
