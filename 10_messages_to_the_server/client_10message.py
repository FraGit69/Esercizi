
import socket as s

udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)



server_address = ("localhost", 6980)
BUFFER_SIZE = 4092 #uanti bit posso inviare o ricevere

for i in range(10):
    udp_client_socket.sendto(f"messaggio numero: {i}".encode('utf-8'), server_address)
