import socket
import ssl
import threading
import logging
import tkinter as tk
from tkinter import simpledialog

logging.basicConfig(level=logging.INFO)

class EncryptedP2PClient:
    def __init__(self):
        self.server_host = None
        self.port = 12345
        self.client_socket = None
        self.nickname = None
        self.gui = None

    def start_client(self):
        if not self.get_server_info():
            return  # Abbruch, wenn die Serverinformationen nicht korrekt sind

        # Versuche eine Verbindung zum Server herzustellen
        if not self.connect_to_server():
            return  # Abbruch, wenn die Verbindung nicht hergestellt werden konnte

        # Starte den Chat
        self.create_gui()

    def get_server_info(self):
        self.server_host = simpledialog.askstring("Server IP", "Enter Server IP:")
        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname:")
        
        # Überprüfe, ob die Server-IP-Adresse gültig ist
        try:
            socket.inet_aton(self.server_host)
        except socket.error:
            logging.error("Invalid server IP address.")
            return False

        return True

    def connect_to_server(self):
        logging.info(f"Attempting to connect to {self.server_host}:{self.port}")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Create an SSL context
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        self.client_socket = context.wrap_socket(s, server_hostname=self.server_host)
        try:
            self.client_socket.connect((self.server_host, self.port))
            logging.info(f"Connected to {self.server_host}:{self.port}")

            # Start a thread to handle incoming messages
            threading.Thread(target=self.handle_client, args=(self.client_socket,)).start()
            return True
        except Exception as e:
            logging.error(f"Error connecting to server: {e}")
            return False

    def handle_client(self, conn):
        try:
            while True:
                msg = conn.recv(1024).decode('utf-8')
                if not msg:
                    break
                logging.info(f"Received: {msg}")
                if self.gui:
                    self.gui.receive_message(msg)
        except Exception as e:
            logging.error(f"Error handling server: {e}")
        finally:
            conn.close()

    def send_message_to_peer(self, message):
        if self.client_socket:
            try:
                full_message = f"{self.nickname}: {message}"
                logging.info(f"Sending message: {full_message}")
                self.client_socket.sendall(full_message.encode())
                # Hier wird die Nachricht zur Anzeige im eigenen Chatfenster hinzugefügt
                if self.gui:
                    self.gui.receive_message(full_message)
            except Exception as e:
                logging.error(f"Error sending message: {e}")

    def create_gui(self):
        root = tk.Tk()
        root.title("P2P Chat Client")

        self.gui = ClientGUI(root, self)
        root.mainloop()

class ClientGUI:
    def __init__(self, root, client_backend):
        self.root = root
        self.client_backend = client_backend

        self.chat_display = tk.Text(root, state=tk.DISABLED)
        self.chat_display.pack(pady=20)

        # Größeres Eingabefeld für die Nachrichten
        self.message_entry = tk.Entry(root, width=60)  # Hier kannst du die Breite anpassen
        self.message_entry.pack(pady=20)

        # Hinzugefügte Bind-Methode, um auf das <Return>-Ereignis zu reagieren
        self.message_entry.bind("<Return>", self.send_message_on_enter)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

        # Fußleiste für Server-IP und Nickname
        self.footer_frame = tk.Frame(root)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.nickname_label = tk.Label(self.footer_frame, text=f"Nickname: {self.client_backend.nickname}")
        self.nickname_label.pack(side=tk.LEFT, padx=10)

        self.server_ip_label = tk.Label(self.footer_frame, text=f"Server IP: {self.client_backend.server_host}")
        self.server_ip_label.pack(side=tk.LEFT, padx=10)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.client_backend.send_message_to_peer(message)
            self.message_entry.delete(0, tk.END)

    def send_message_on_enter(self, event):
        self.send_message()

    def receive_message(self, message):
        self.chat_display.configure(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.configure(state=tk.DISABLED)

if __name__ == "__main__":
    client = EncryptedP2PClient()
    client.start_client()
