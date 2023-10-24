# use sqlite3
import sqlite3

# import pm2
#import pm2

# import time
import time

# pip install paramiko
import paramiko

# tornado
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

# watchdog to monitor file change in the sftp server remote directory
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# declare ip and port

#IP = '192.168.242.146' 
#PORT = 22

# connect to the sftp server
'''
try:
    privatekeyfile = 'assignment_base\id_rsa.ppk'
    mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
    transport = paramiko.Transport((IP, PORT))
    transport.connect(username = 'camera1', pkey = mykey)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("Connected to sftp server at " + IP + ":" + str(PORT)) 
except Exception as e:
    print("Unable to connect to the sftp server")
    print(e)
    exit()
'''
# connect to the sqlite3 database









# monitor the remote directory for changes in the home/camera1/Public/Footage/ directory
class Watcher:
    # watch the remote directory for changes
    
    DIRECTORY_TO_WATCH = '/home/camera1/Public/Footage/'

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print ("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()






