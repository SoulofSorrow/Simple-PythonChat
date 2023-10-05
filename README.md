# Sichere P2P-Chat-Anwendung

Dieses Python-Programm implementiert eine sichere P2P-Chat-Anwendung mit einer verschlüsselten Kommunikation zwischen den Teilnehmern. Die Anwendung besteht aus einem Client- und einem Server-Teil und ermöglicht das Senden und Empfangen von Nachrichten in Echtzeit.

## Client-Seite
- Der Client kann sich mit einem Server verbinden und Nachrichten an andere verbundene Clients senden.
- Die Benutzeroberfläche des Clients ist in Tkinter implementiert und bietet ein Chat-Fenster sowie die Möglichkeit, Nachrichten zu senden.

## Server-Seite
- Der Server wartet auf eingehende Verbindungen von Clients und leitet Nachrichten zwischen den Clients weiter.
- Die Kommunikation zwischen Client und Server ist verschlüsselt, um die Sicherheit der übertragenen Daten zu gewährleisten.

## Voraussetzungen
- Python 3.x
- Die `tkinter`-Bibliothek für die Benutzeroberfläche des Clients
- Zertifikate `cert.pem` und `key.pem` für die verschlüsselte Kommunikation auf der Serverseite

## Anleitung
1. Starten Sie den Server mit dem `EncryptedP2PServer.py`-Skript, wobei Sie optional das `--debug`-Flag verwenden, um Chat-Nachrichten auf dem Server anzuzeigen.
2. Starten Sie den Client mit dem `EncryptedP2PClient.py`-Skript. Sie werden nach der Server-IP und einem Nickname gefragt.
3. Geben Sie Nachrichten im Client ein und senden Sie sie an andere verbundene Clients.
4. Die Kommunikation erfolgt verschlüsselt und sicher.

**Hinweis:** Dieses P2P-Chat-Programm wurde entwickelt, um eine sichere Kommunikation zwischen den Teilnehmern zu ermöglichen. Stellen Sie sicher, dass die erforderlichen Zertifikate vorhanden sind und die Server-IP korrekt angegeben ist.

