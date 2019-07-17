from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
from threading import Thread
import logging
import cgi
import sys


class HttpServerHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.get_method = self.get_method_dummy
        self.post_method = self.post_method_dummy
        BaseHTTPRequestHandler.__init__(self, *args)

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def get_method_dummy(self):
        return 'dummy'

    def pass_get_method(self, get_method):
        self.get_method = get_method

    def do_GET(self):
        self._set_headers()
        print self.get_method()
        print self.path
        print parse_qs(self.path[2:])
        header = "<html><body><h1>Get Request Received!"
        footer = "</h1></body></html>"
        resp = header + self.server.handler() + footer
        self.wfile.write(resp)

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
        # print form.getvalue("foo")
        # print form.getvalue("bin")
        resp = "<html><body><h1>POST Request Received!</h1></body></html>"
        self.wfile.write(resp)


class MyHTTPServer(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, handler):
        HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self.handler = handler


class HttpServer:
    def __init__(self, name, host, port, handler):
        self.name = name
        self.host = host
        self.port = port
        self.handler = handler
        self.server = None

    def start(self):
        logging.info(
            'Starting %s at %s:%d' % (self.name, self.host, self.port))
        # we need use MyHttpServer here
        self.server = MyHTTPServer((self.host, self.port), HttpServerHandler,
                                   self.handler)
        self.server.serve_forever()

    def stop(self):
        if self.server:
            logging.info('Stopping %s at %s:%d' % (self.name, self.host,
                                                   self.port))
            self.server.shutdown()


def server_handler():
    return "uga"


class Server:
    def __init__(self, config):
        self.config = config
        self.thread = None
        self.httpd = None
        self.port = int(self.config.get_local_port())
        self.debug = int(self.config.get_debug())
        logging.basicConfig(
            format='%(asctime)s [%(levelname)s] %(message)s',
            level=logging.INFO)

    def run(self, port):
        self.server = HttpServer(
            "test server", "localhost", port, server_handler)
        self.server.start()

    def stop(self):
        self.server.stop()

    def run_thread(self):
        self.run(self.port)
