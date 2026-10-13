from nodo import Nodo

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.__tamano = 0

    def encolar(self, data):
        nuevo_nodo = Nodo(data, None)
        if self.esta_vacia():
            self.frente = nuevo_nodo
        else:
            self.final.next = nuevo_nodo
        self.final = nuevo_nodo
        self.__tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        dato = self.frente.data
        self.frente = self.frente.next
        if self.frente is None:
            self.final = None
        self.__tamano -= 1
        return dato

    def esta_vacia(self):
        return self.frente is None