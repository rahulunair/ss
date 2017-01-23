#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
"""A simple HTTP server that prints out the path, headers and
content for different requests."""
PORT = 7979


class HandleRequests(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write("Echoing GET request...")
        print("Path: {}".format(self.path))
        print("Headers: {}".format(self.headers))
        print("End of request...")

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write("Echoing GET request...")
        print("Path: {}".format(self.path))
        print("Content: {}".format(self.content))
        print("Headers: {}".format(self.headers))
        print("End of request...")

    do_PUT = do_POST
    do_DELETE = do_GET


def start():
    print("ss listening on {}".format(PORT))
    server = HTTPServer(("", PORT), HandleRequests)
    server.serve_forever()

if __name__ == "__main__":
    start()
