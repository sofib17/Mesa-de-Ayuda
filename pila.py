from nodo import Nodo

class Pila:
    def __init__(self):
        self.cima = None
        self.__tamano = 0

    def apilar(self, data):
        nuevo_nodo = Nodo(data, self.cima)
        self.cima = nuevo_nodo
        self.__tamano += 1

    def desapilar(self):
        if self.esta_vacia():
            return None
        dato = self.cima.data
        self.cima = self.cima.next
        self.__tamano -= 1
        return dato

    def consultar_cima(self):
        if self.esta_vacia():
            return None
        return self.cima.data

    def esta_vacia(self):
        return self.cima is None