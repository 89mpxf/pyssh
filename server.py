"""
Python SSHv2 Server
Written by: 89mpxf
https://github.com/89mpxf/pyssh
"""

# Import dependencies
from sys import argv

# Import local dependencies
from src.runtime import run_server

if __name__ == "__main__":
    run_server(*argv[1:])