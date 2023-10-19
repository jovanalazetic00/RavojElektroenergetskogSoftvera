from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class Add_script:   #za manuelno i automatsko dodavanje workera

    @staticmethod
    def manual_adding(msg, db='RES_PROJEKAT'):
        _db = DatabaseCRUD('127.0.0.1', 'admin', 'admin', db)  #kad hocemo manuelno da dodajemo pozivamo databaseCRUD, instanciramo ga

        _tokens = msg.split(':')  #splitujemo sta je korisnik poslao po :
        _id = _tokens[1]  #prvi token je id

        _ret = _db.get_brojilo(_id)  #dobavljamo brojilo pomocu databaseCRUD sa tim id-em
        if not _ret:
            print("[MAIN THREAD] Brojilo sa id='{id}' ne postoji!".format(id=_id))  #ako brojilo ne postoji onda smo u main tredu i ispisemoda ne postoji ne mozemo dodati brojilo
            return -1
        else:
            _mesec = _tokens[2]  #ako postoji uzimamo mjesec, i on se nalazi na tokenu 2
            _ret = _db.get_potrosnja_brojila(_id, _mesec)  #pokusamo da dobavimo brojilo sa kljucevima id, i mjesec, ako postoji ispisujemo else dole

            if not _ret:  #ako ne postoji
                _potrosnja = _tokens[3]  #sa treceg tokena uzimamo kolika je potrosnja
                _ret = _db.insert(_id, _mesec, _potrosnja)  #izvrsavamo dataBase insert, saljemo mjesec i potrosnju
                if _ret == 1:  #ako vrati 1
                    _ret = f"Successfully inserted '{_id} {_mesec} {_potrosnja}'"  #uspjesno je insertovao
                print("[MAIN THREAD] {ret}!".format(ret=_ret))
                return 0
            else:
                print("[MAIN THREAD] Merenje brojila id:mesec='{id}:{mesec}' vec postoji!".format(id=_id, mesec=_mesec))  #mjerenje sa id i mjesec vec postoji
                return -2

    @staticmethod
    def automatic_adding(msg, buffer):  #posaljemo poruku
        buffer.append(msg)  #dodamo u bafer poruku koju je klijent poslao
        return len(buffer)
