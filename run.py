#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class MyRequestHandler(BaseHTTPRequestHandler):

    # get an client IP
    def get_client_ip(self):
        client_ip = self.client_address[0]
        return client_ip

    # rewrite GET request
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send message back to client
        message = str(self.headers.get('X-Forwarded-For')) + str('\n')
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('starting server...')
    # Server settings
    server_address = ('0.0.0.0', 8081)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('running server port 8081 ...')
    httpd.serve_forever()

run()