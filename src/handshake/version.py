# Import dependencies
from platform import python_version_tuple

def server_version() -> bytes:
    return "SSH-2.0-Python_{}.{}.{}\r\n".format(*python_version_tuple()).encode()