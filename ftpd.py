import os
import sys
import tempfile
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.filesystems import UnixFilesystem


def on_file_received(handler, file):
    print('remove file:'+file)
    os.remove(file)

def main(port):
    # create a temp directory and store downloaded files in the temp directory.
    with tempfile.TemporaryDirectory() as tmpdirname:
        authorizer = DummyAuthorizer()
        authorizer.add_user('ftp', 'ftppasswd', tmpdirname, perm='elradfmwMT')
        handler = FTPHandler
        handler.authorizer = authorizer
        handler.abstracted_fs = UnixFilesystem
        handler.on_file_received = on_file_received
        server = FTPServer(('', port), handler)
        server.serve_forever()

if __name__ == "__main__":
    port = 21
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])

    main(port)

