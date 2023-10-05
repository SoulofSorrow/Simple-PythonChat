import socket
import ssl
import threading
import logging
import argparse

logging.basicConfig(level=logging.INFO)

class EncryptedP2PServer:
    def __init__(self, host, port, debug=False):
        self.host = host
        self.port = port
        self.debug = debug
        self.clients = []  # List to keep track of connected clients

    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)  # Allow up to 5 pending connections
        logging.info(f"Listening for connections on {self.host}:{self.port}")
        
        while True:
            conn, addr = s.accept()
            logging.info(f"Connection from {addr}")
            
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
            ssl_conn = context.wrap_socket(conn, server_side=True)
            
            self.clients.append(ssl_conn)  # Add the new client to the list
            threading.Thread(target=self.handle_client, args=(ssl_conn,)).start()

    def handle_client(self, conn):
        try:
            while True:
                msg = conn.recv(1024).decode('utf-8')
                if not msg:
                    break
                if self.debug:
                    logging.info(f"Message from {conn.getpeername()}: {msg}")
                self.broadcast_message(msg, conn)
        except Exception as e:
            logging.error(f"Error handling client: {e}")
        finally:
            conn.close()
            self.clients.remove(conn)  # Remove the client from the list

    def broadcast_message(self, message, sender_conn):
        """Send the message to all clients except the sender."""
        for client in self.clients:
            if client != sender_conn:
                try:
                    client.sendall(message.encode())
                except Exception as e:
                    logging.error(f"Error broadcasting message to {client.getpeername()}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start the encrypted P2P server.")
    parser.add_argument("--debug", action="store_true", help="Display chat messages on the server.")
    args = parser.parse_args()

    server = EncryptedP2PServer('localhost', 12345, debug=args.debug)
    server.start_server()
