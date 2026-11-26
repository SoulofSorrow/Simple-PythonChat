# Architecture

## File map

| Path | Content |
| --- | --- |
| `backend.py` | `EncryptedP2PServer`: `start_server()`, `handle_client()`, `broadcast_message()`; CLI flag `--debug` |
| `client_backend.py` | `EncryptedP2PClient` (connect, receive thread, send) and `ClientGUI` (Tkinter window) |
| `cert.pem`, `key.pem` | Server TLS certificate and private key, loaded from the working directory |
| `README.md` | German user description |
| `LICENSE.md` | GNU GPL |

## Server (`backend.py`)

1. Binds `localhost:12345` (hardcoded in `__main__`), `listen(5)`.
2. Per accepted connection: new `ssl.create_default_context(CLIENT_AUTH)`,
   `load_cert_chain("cert.pem", "key.pem")`, wrap server side, append to
   `self.clients`, start a thread running `handle_client()`.
3. `handle_client()`: `recv(1024)`, UTF-8 decode, log the message when
   `--debug`, `broadcast_message()` to all other clients. On disconnect or
   error the socket is closed and removed from `self.clients`.

## Client (`client_backend.py`)

1. Tkinter dialogs ask for server IP (validated with `socket.inet_aton`, IPv4
   only) and nickname.
2. TLS connect to port `12345` with `check_hostname = False` and
   `verify_mode = ssl.CERT_NONE`.
3. Receive thread appends incoming text to the chat window.
4. Sending prefixes `<nickname>: `, sends the text and echoes it locally.

## Protocol

- Raw UTF-8 text over TLS, no framing; one `recv(1024)` per message.
- The server does not add sender information; the client includes the
  nickname in the text.

## Known issues

- Server listens on `localhost` only, so remote clients cannot connect
  without code changes.
- Client does not verify the server certificate.
- `README.md` names `EncryptedP2PServer.py` / `EncryptedP2PClient.py`; the
  files are `backend.py` / `client_backend.py`.
- `self.clients` is modified from several threads without a lock.
- The Tkinter UI is updated from the receive thread.
