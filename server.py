from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # If the path doesn't end with .html and doesn't have a file extension
        if not '.' in self.path and not self.path.endswith('/'):
            # Try to serve the corresponding .html file
            if os.path.exists(self.path.lstrip('/') + '.html'):
                self.path = self.path.lstrip('/') + '.html'
                return SimpleHTTPRequestHandler.do_GET(self)
            # If the file doesn't exist, try index.html
            elif self.path == '/':
                self.path = 'index.html'
                return SimpleHTTPRequestHandler.do_GET(self)
            else:
                self.send_error(404, "File not found")
                return
        return SimpleHTTPRequestHandler.do_GET(self)

    def translate_path(self, path):
        # Remove leading slash
        path = path.lstrip('/')
        # If path is empty, serve index.html
        if not path:
            path = 'index.html'
        return path

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run() 