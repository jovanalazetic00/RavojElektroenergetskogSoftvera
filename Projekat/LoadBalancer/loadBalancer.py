import socket
import threading
import time

from Scripts.worker_script import Worker_script
from Scripts.add_script import Add_script

from Projekat.Worker.worker import Worker


class LoadBalancer:

    def __init__(self):
        self.port = 8000
        self.server = socket.gethostbyname(socket.gethostname())
        self.address = (self.server, self.port)
        self.format = 'utf-8'

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.address)

        self.workers = []
        self.number_of_workers = 1
        self.buffer = list()

    def handle(self, conn, addr): #conn konekcija otvorena sa klijentom i adresa klijenta
        print(f'[NEW CONNECTION] {addr} connected.')

        is_connected = True

        while is_connected:
            _msg = conn.recv(1024).decode(self.format)  #ceka na poruku od klijenta i obradjuje je kad stigne
            if _msg:  #ako je null
                if _msg == '!DISC':
                    is_connected = False
                elif 'Manual' in _msg:
                    Add_script.manual_adding(_msg)
                elif 'Name ' in _msg:   #ako je pristigla poruka ime workera on se terminira
                    self.number_of_workers = Worker_script.terminate_worker(_msg.split()[1], self.workers,
                                                                            self.number_of_workers)
                elif _msg == 'add':  #automatsko dodavanje preko workera
                    self.number_of_workers = Worker_script.new_worker(self.number_of_workers, self.workers)
                    self.buffer_check()
                else:
                    Add_script.automatic_adding(_msg, self.buffer)
                    self.buffer_check()

        print(f'[THREAD {threading.current_thread().ident}] Terminated')
        conn.close()

    def start(self):
        self.server.listen()
        print(f'[LISTENING] server listening at {self.address}...')
        _worker = Worker("WORKER_0")  #koristimo konstruktor workera
        _t = threading.Thread(target=_worker.start_worker, name=f'WORKER_0')
        _t.start()
        self.workers.append(_worker)
        while True:
            _conn, _addr = self.server.accept()  #ceka novu konekciju
            _thread = threading.Thread(target=self.handle, args=(_conn, _addr))  #kreira se novi tred
            _thread.start()

    def buffer_check(self):

        if len(self.buffer) >= 10:
            _in = self.add_to_temp(self.buffer)
            _done = False

            while not _done:
                for _worker in self.workers:
                    _done = self.is_worker_free(_worker, _in)
                if not _done:
                    time.sleep(2)
            self.clear_buffer(_in)

    def is_worker_free(self, worker, msg):
        if worker.check():  #chech properti u klasi worker
            worker.queue_put(msg)  #ako je slobodan stavlja por u red
            return True
        return False

    def clear_buffer(self, buffer):
        for _item in buffer:
            self.buffer.remove(_item)

    def add_to_temp(self, buffer):
        _in = list()
        for _item in buffer:
            _in.append(_item)
            if len(_in) == 10:
                break
        return _in
def main():
    _server = LoadBalancer()
    _server.start()


if __name__ == '__main__':
    main()
