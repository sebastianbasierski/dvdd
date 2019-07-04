from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
from threading import Thread
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

class Server:
    def __init__(self, port):
        self.thread = None
        self.httpd = None
        self.port = port

    def run(self, server_class=HTTPServer, handler_class=GP, port=8080):
            server_address = ('', port)
            self.httpd = server_class(server_address, handler_class)
            print 'Server running at localhost:' + str(port) + '...'
            self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()

    def run_thread(self):
        self.run(HTTPServer, GP, self.port)

