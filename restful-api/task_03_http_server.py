#!/usr/bin/python3
''' Module that implements a simple API '''

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    ''' Handler for HTTP requests '''

    def do_GET(self):
        """gérer les différents endpoint avec code 200"""
        # Log pour afficher la requête reçue
        print(f"Requête reçue: {self.command} {self.path}") 

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")  # str en bytes

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                'name': 'John Doe',
                'age': 30,
                'city': 'New York'
            }
            self.wfile.write(bytes(json.dumps(data), "utf8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {
                'status': 'OK'
            }
            self.wfile.write(bytes(json.dumps(status), "utf8"))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                'version': '1.0',
                'description': 'A simple API built with http.server'
            }
            self.wfile.write(bytes(json.dumps(info), "utf8"))

        else:
            """gérer les endpoints failed"""
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not found')

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    ''' Starts the HTTP server '''
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()