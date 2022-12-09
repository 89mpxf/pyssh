# Import local dependencies
from .create_server import create_server
from .session.session import create_session, start_session
from .session.manager import SessionManager

def run_server(host: str = "0.0.0.0", port: int = 26581):
    server = create_server(host, port)
    print(f"Server now listening on {host}:{port}")
    server.listen(5)
    sm = SessionManager()
    while True:
        conn, addr = server.accept()
        print(f"Connection initialized from {addr[0]}:{addr[1]}")
        start_session(session := create_session(sm, conn, addr))
        sm.append(session)