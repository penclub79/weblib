from http.server import BaseHTTPRequestHandler, HTTPServer
#핸들은 BaseHTTPRequestHandler로 http의 기본적인 응답을 할수 있는 기능들이 들어있다.
port = 9999
#상속받는 핸들러를 실행하라
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # print('receive result')
        #응답만들기
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=urf-8')
        self.end_headers()
        self.wfile.write('<h1>Hello World</h1>'. encode('utf-8'))

#서버구동
httpd = HTTPServer(('', 9999), MyHTTPRequestHandler)
#서버주소랑 포트랑 등록한다.
print('HTTP Server Starts....')
httpd.serve_forever()   #
'''
serve_forever()메서드를 실행하면 서버는 요청을 기다리게 된다.
그리고 요청이 들어오면 등록된 핸들러에 요청정보를 전달해준다.
'''