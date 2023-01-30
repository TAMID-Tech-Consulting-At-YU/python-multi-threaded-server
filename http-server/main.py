import pickle
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
server_port = 9000
members = []


class Server(BaseHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer) -> None:
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path == '/getMembers':
            serialized = pickle.dumps(members)
            self.wfile.write(bytes(serialized))

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        if self.path == '/addMember':
            member = pickle.loads(post_body)
            self.add_member(member)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("User added", "utf-8"))

    def add_member(self, member):
        members.append(member)

    def get_members(self):
        return members


if __name__ == "__main__":
    webServer = HTTPServer((host_name, server_port), Server)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
