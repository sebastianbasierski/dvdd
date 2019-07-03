from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
from threading import Thread
import signal
import time
import cgi
import sys

class GP(BaseHTTPRequestHandler):
	def __init__(self, *args):
                self.get_method = self.get_method_dummy
                self.post_method = self.post_method_dummy
		BaseHTTPRequestHandler.__init__(self, *args)

	def _set_headers(self):
		self.send_response(200)
	        self.send_header('Content-type', 'text/html')
	        self.end_headers()
	
	def do_HEAD(self):
		self._set_header()

	def get_method_dummy(self):
		return 'dummy'

	def pass_get_method(self, get_method):
		self.get_method = get_method

	def do_GET(self):
        	self._set_headers()
		print self.get_method()
	        print self.path
	        print parse_qs(self.path[2:])
	        self.wfile.write("<html><body><h1>Get Request Received!</h1></body></html>")

	def post_method_dummy(self):
		return 'dummy'

	def pass_post_method(self, post_method):
		self.post_method = post_method

	def do_POST(self):
	        self._set_headers()
	        form = cgi.FieldStorage(
	        	fp=self.rfile,
		        headers=self.headers,
		        environ={'REQUEST_METHOD': 'POST'}
		)
	        print form.getvalue("foo")
	        print form.getvalue("bin")
	        self.wfile.write("<html><body><h1>POST Request Received!</h1></body></html>")

httpd = 0
def run(server_class=HTTPServer, handler_class=GP, port=8080):
        global httpd
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print 'Server running at localhost:' + str(port) + '...'
        httpd.serve_forever()

def close():
        global httpd

        httpd.shutdown()

def run_thread():
        run(HTTPServer, GP, 8079)

def signal_handler(sig, frame):
        global thread

        print 'ctrl + c'
        close()
        thread.join()
        sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
thread = Thread(target=run_thread, args=())
thread.start()
while True:
        signal.pause()

