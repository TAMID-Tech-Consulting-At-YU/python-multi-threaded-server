import logging
import socket


class Server(object):

    def __init__(self, configuration) -> None:
        super().__init__()
        self.config = configuration
        self.logger = logging.getLogger(__name__)
        self.log_server_info()
        self.is_running = False
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()

    def start(self):
        if self.is_running:
            return
        host = self.config.get_host()
        port = self.config.get_port()
        self.logger.debug(f"Binding to {(self.config.get_host(), self.config.get_port())}")
        server_socket = self.server

        # TODO this will be to complete
        server_socket.bind((host, port))
        server_socket.listen()
        while True:
            conn, address = server_socket.accept()
            self.logger.info("Connection from: " + str(address))
            self.start_client_task(conn)
            self.logger.info("Closing connection from: " + str(address))
            conn.close()

    def stop(self):
        self.logger.info("Shutting down server")
        self.is_running = False
        self.server.close()

    def start_client_task(self, conn):
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())

    def log_server_info(self):
        self.logger.info(f"Starting server: \n("
                         f"HOST: {self.config.get_host()}"
                         f"\nPORT: {self.config.get_port()}"
                         f")")

    def __repr__(self) -> str:
        return super().__repr__()

    def __del__(self):
        if self.is_running:
            self.stop()
