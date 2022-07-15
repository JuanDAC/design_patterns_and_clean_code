from abc import ABC, abstractmethod
from typing import List

""" interface Subject """


class Subject(ABC):
    @abstractmethod
    def register(self, obj):
        pass

    @abstractmethod
    def remove(self, obj):
        pass

    @abstractmethod
    def notify(self, event):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass


""" Concrete Subject """


class NumberHandler(Subject):
    _singleton = None
    suscribed: List[Observer] = []

    @classmethod
    def getInstance(cls):
        if cls._singleton is None:
            cls._singleton = NumberHandler()
        return cls._singleton

    def register(self, obj: Observer):
        self.suscribed.append(obj)

    def remove(self, obj: Observer):
        self.suscribed.remove(obj)

    def notify(self, event):
        for obsever in self.suscribed:
            obsever.update(event)


class Binary(Observer):
    def update(self, number):
        print('Bynary in ' + bin(number))


class Decimal(Observer):
    def update(self, number):
        print('Decinal in ' + str(int(number)))


class Hexadecimal(Observer):
    def update(self, number):
        print('Hexadecimal in ' + hex(number))



binaryHandler = Binary()
NumberHandler.getInstance().register(binaryHandler)
NumberHandler.getInstance().register(Decimal())
NumberHandler.getInstance().notify(15)
print('-----------------------------------------------------')
NumberHandler.getInstance().register(Hexadecimal())
NumberHandler.getInstance().remove(binaryHandler)
NumberHandler.getInstance().notify(10)

