from abc import ABC, abstractmethod  #abc importujemo apstraktne klase


class CRUD(ABC):  #nasljedjujemo apstraktnu klasu, i time ona postaje apstraktna

    @abstractmethod  #apstraktne metode nemaju implementaciju
    def read(self, *args):  #*args znaci da read moze primiti proizvoljan broj argumenata
        pass

    @abstractmethod
    def insert(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass

    @abstractmethod
    def update(self, *args):
        pass
