from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt


PORT = 9999

#상속받는 핸들러를 실행하라
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    #MyHTTPRequestHandler는 상속받은 클래스이다.
    def do_GET(self):   #파라미터를 가져오자

        qindex = self.path.find('?')

        if qindex == -1:
            req_url = self.path[:len(self.path)]
        else:
            req_url = self.path[:qindex]
        # print(qindex)

        if req_url != '/graph':
            self.send_error(404, 'FileNot Found')
            return

        # print(req_url)    #절대 경로(path) /graph?a=10&b=20에서 /graph만 나오게하기
        handler_name = 'ex' + self.get_parameter('ex')
        if handler_name not in MyHTTPRequestHandler.__dict__:
            self.send_error(404, 'FileNot Found')
            return

        MyHTTPRequestHandler.__dict__[handler_name](self)
        # print(ex)
    def get_parameter(self, name):
        qindex = self.path.find('?')

        if qindex == -1:
            qs = ''
        else:
            qs = self.path[qindex+1:]

        params = parse_qs(qs)
        values = params.get(name)

        return None if values is None else values.pop() #삼항연산자
        # print(params)


    def ex1(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=urf-8')
        self.end_headers()
        self.wfile.write('<h1>Hello World</h1>'.encode('utf-8'))

    def ex2(self):
        arr = np.random.normal(5, 3, 500)

        fig, subplots = plt.subplots(2, 1)
        subplots[0].plot(arr, color='red', linestyle='solid')
        subplots[1].hist(arr, bins=20, edgecolor='black', linewidth=1.2)

        buffer = BytesIO()
        plt.savefig(buffer, dpi = 80, bbox_inches='tight')
        plt.clf()   #메모리에 플러스가된다.

        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        self.wfile.write(buffer.getvalue())

#서버구동
httpd = HTTPServer(('', PORT), MyHTTPRequestHandler)
print('HTTP Server Runs on Port(%d)' %  (PORT))
httpd.serve_forever()
