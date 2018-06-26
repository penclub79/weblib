from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser):  #상속을 받을수 있다.
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
# def parseimage(data):
#     parser = ImageParser()
#     parser.feed(data)   #자동으로 파싱됩니다.    feed는 상속받음
#     dataset = set(x for x in parser.result) #set집합으로 만듦
#     print('\n'.join(sorted(dataset)))

def main():
    url = 'http://www.google.co.kr'
    response = urlopen(url)
    # print(response)
    charset = response.headers.get_content_charset()
    # print(charset)
    data = response.read().decode(charset)
    # print(data)
    response.close()

    # print(data)

    # print('\n>>>>>>>>>> Fetch Image from', url)

    parser = ImageParser()
    parser.feed(data)   #자동으로 파싱됩니다.    feed는 상속받음
    dataset = set(x for x in parser.result) #set집합으로 만듦
    # print('\n'.join(sorted(dataset)))

    # parseimage(data)

if __name__ == '__main__':
    main()