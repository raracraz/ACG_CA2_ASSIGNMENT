# use sqlite3
import sqlite3

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






