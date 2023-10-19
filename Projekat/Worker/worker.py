import threading
import time
from queue import Queue
from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class Worker:  #ne pravimo konstruktore, jer smo ga iskoristili uloadBalanceru kad smo ga kreirali

    def __init__(self, name):
        self.q = Queue()  #kreira se njegov queue
        self.is_free = True  #postavi se da je slobodan
        self.name = name  #postavi se njegovo ime
        self.db = DatabaseCRUD()  #instancira se databaseCrud da mozemo da radimo sa bazom

    def start_worker(self):  #izvrsava se u tredu workera
        while True:
            self.is_free = True
            print("[{name}] is free".format(name=threading.current_thread().name))  #ispisemo inicijalno da je worker slobodan
            item = self.q.get()  #blokirajuca operacija, upisivanje u red
            self.is_free = False  #postavi se da je zauzet
            if item == "!TERM":  #ako je stigao zahtjev koji treba da se obradi
                break
            print("[{name}] is busy".format(name=threading.current_thread().name))  #ispisujemo poruku da je zauzet
            print("[{name}] Message received: {msg}".format(name=threading.current_thread().name, msg=item))  #ispise koje sve poruke je primio, onih 10
            for i in item:  #prolazi kroz sve poruke koje je primio
                self.do_work(i)  #poziva do work   #poziva 10 puta do work za svaki item
                time.sleep(5)  #spava 5 s
            if item is None:
                self.q.task_done()  #kad zavrsi sa itemima task je gotov
                break
        return 0

    def queue_put(self, q):  #stavljanje u queue, poziva se iz add skripte
        self.q.put(q)

    def check(self):
        return self.is_free

    def do_work(self, item):
        print("[{name}] Processing message '{msg}'".format(name=threading.current_thread().name, msg=item))  #ispise koju poruku trenutno procesira
        tokens = item.split()  #splituje tokene
        id_brojila = tokens[0]  #na nultom mjestu je id brojila
        _suc = "[{name}] Message processed '{msg}'\n".format(name=threading.current_thread().name, msg=item)
        res = self.db.get_brojilo(id_brojila)
        if res:
            mesec = tokens[1]
            res = self.db.get_potrosnja_brojila(id_brojila, mesec)  #da  li postoji brojilo
            if res:  #ako brojilo postoji ispisemo
                print("[{name}] '{item}' already exists".format(name=threading.current_thread().name, item=item))
                print(_suc)
                return -2
            else:
                potrosnja = tokens[2]  #ako brojilo ne pstoji, parsiramo i potrosnju
                _msg = self.db.insert(id_brojila, mesec, potrosnja)  #vrsimo insert dodavanje
                if _msg == 1:
                    _msg = f"Successfully inserted '{id_brojila} {mesec} {potrosnja}'"  #ako je uspjesno insertovao ubacimo
                print("[{name}] {msg}".format(name=threading.current_thread().name, msg=_msg))
        else:
            print("[{name}] unknown id = '{id}'".format(name=threading.current_thread().name, id=id_brojila))  #ako brojilo ne postoji, ispisemo da je id nepoznat i zavrsimo sa procesiranjem zahtjeva
            print(_suc)
            return -1
        print(_suc)
        return 0
       
