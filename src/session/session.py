# Import dependencies
from threading import Thread
from socket import socket

# Import local dependencies
from ..handshake.start import handshake

class ClientSession(Thread):
    def __init__(self, session_manager, sock: socket, addr: tuple):
        Thread.__init__(self)
        self.daemon = True
        self.session_manager = session_manager
        self.sock = sock
        self.addr = addr

    def run(self):
        handshake(self.sock)

def create_session(session_manager, sock: socket, addr: tuple) -> Thread:
    return ClientSession(session_manager, sock, addr)

def start_session(session: ClientSession):
    return session.start()