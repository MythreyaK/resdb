from logging import log
import multiprocessing
from multiprocessing import Queue
from os import terminal_size
import socket
import time
from resdb import app

# Queue for log
log_queue = Queue()

def get_log():
    while True:
        yield log_queue.get()

class Socket:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = None
        self.buff_size = 1024 # bytes

    def init(self):
        print("In init")
        if not self.sock:
            print("Creating as not created")
            self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self.sock.bind((self.ip, self.port))
        print("Init done")

    def listen(self, queue):
        try:
            while(True):
                bytesAddressPair = self.sock.recvfrom(self.buff_size)
                message = bytesAddressPair[0]
                address = bytesAddressPair[1]

                # log_line = str.format("Message: {}, From Address {}\n", message, address);
                print(str(message))
                try:
                    queue.put(str(message))
                except:
                    print("WARN: Logger queue is full: ", queue.qsize())
                    pass
        except KeyboardInterrupt:
            pass
        finally:
            if self.sock:
                self.sock.close()

def start_listen_process():
    print("Start called")
    socket = Socket(app.config["LOGGER_LISTEN_IP"], app.config["LOGGER_LISTEN_PORT"])
    socket.init()

    socket_process = multiprocessing.Process(target = socket.listen, args=(log_queue,))
    socket_process.daemon = True
    socket_process.start()
    print("Process started")
