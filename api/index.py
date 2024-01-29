from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler): # subclass of BaseHTTPRequestHandler
    # WRRC
    def do_GET(self):
        
        message = "Please provide a country or capital name"
            
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        self.wfile.write(message.encode('utf-8'))
        return