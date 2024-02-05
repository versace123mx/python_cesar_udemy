import socket
import socketserver
import urllib.request

servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.connect(('8.8.8.8',80))

print(f"La ip es {servidor.getsockname()[0]}")
print(f"La ip del router {socket.gethostbyname(socket.gethostname())}")
print(f"nombre del equipo {socket.gethostname()}")
servidor.close()
