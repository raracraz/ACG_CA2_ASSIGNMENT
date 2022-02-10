# need to pip install pytftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# use sftp 


# for the blockchain class
import hashlib
import json
from time import time

# for tornado web server
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.template
calculate_path = "assignment_base\source\server\data"

# for the database class
import sqlite3
dbName = 'raraDB.db'
#modules used: tornado, hashlib, time, json

# import RSA
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
# import DSA
import cryptography.hazmat.primitives.asymmetric.dsa as dsa




'''
authorizer = DummyAuthorizer() # handle permission and user
authorizer.add_anonymous("assignment_base\source\server\data" , perm='adfmwM')
handler = FTPHandler #  understand FTP protocol
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 2121), handler) # bind to high port, port 21 need root permission
server.serve_forever()
'''

# Http class using tornado
class HttpHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hihi")

def make_app():
    return tornado.web.Application([
        (r"/", HttpHandler),
    ])

class UploadFile(tornado.web.RequestHandler):

    def put(self, params):
        path = calculate_path(params)
        with open(path, 'wb') as out:
            body = self.request.get_argument('data')
            out.write(bytes(body, 'utf8'))

# Blockchain class
class Blockchain(object):
    def __init__(self) -> None:
        self.chain = []
        self.currentFootage = []

        self.newBlock(previous_hash="LUCAS, JEDI, RYAN AND THE LAST JEDI", proof=100)

    def newBlock(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            #put timestamp as data month year format
            'timestamp': time(),
            'proof': proof,
            'footage': self.currentFootage,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.currentFootage = []
        self.chain.append(block)

        return block

    @property
    def lastBlock(self):
        return self.chain[-1]

    def newFootage(self, footage, sender, recipient):
        footage ={
            'footage': footage,
            'sender': sender,
            'recipient': recipient,
        }
        self.currentFootage.append(footage)

        return self.lastBlock['index'] + 1
    
    def hash(self, block):
        stringObject = json.dumps(block, sort_keys=True)
        blockString = stringObject.encode()

        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()

        return hexHash

class raraDB:
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.cur = self.conn.cursor()

    def createTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS footage(txid TEXT PRIMARY KEY, addr TEXT, dateTime TEXT)")

    def insertData(self, addr, dateTime):
        self.cur.execute("INSERT INTO footage VALUES(NULL, ?, ?)", (addr, dateTime))
        self.conn.commit()

    def searchData(self, addr):
        self.cur.execute("SELECT * FROM footage WHERE addr=?", (addr,))
        return self.cur.fetchone()

    def deleteData(self, addr):
        self.cur.execute("DELETE FROM footage WHERE addr=?", (addr,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()