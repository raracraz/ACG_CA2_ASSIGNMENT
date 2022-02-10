# need to pip install pytftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
# use sqlite3
import sqlite3

# import pm2
#import pm2

# pip install pysftp
import pysftp

# tornado
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

# ssh keygen



authorizer = DummyAuthorizer() # handle permission and user
authorizer.add_anonymous("source\server\data" , perm='adfmwM')
handler = FTPHandler #  understand FTP protocol
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 2121), handler) # bind to high port, port 21 need root permission
server.serve_forever()


