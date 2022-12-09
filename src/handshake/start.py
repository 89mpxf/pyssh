# Import dependencies
from socket import socket

# Import local dependencies
from .version import server_version

def handshake(sock: socket):
    sock.send(server_version())