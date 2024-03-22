import http.server
import socketserver
port = 8080
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",port), handler) as server:
    print(f"Serving on port {port}")
    server.serve_forever() 