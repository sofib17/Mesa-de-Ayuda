from cola import Cola
from pila import Pila
from solicitud import Solicitud

class MesaAyuda:
    def __init__(self):
        self.pendientes = Cola()
        self.historial = Pila()

    def registrar_solicitud(self, id_s, usuario, desc):
        nueva = Solicitud(id_s, usuario, desc)
        self.pendientes.encolar(nueva)
        print("¡Solicitud registrada y agregada a la cola de pendientes con éxito!")

    def atender_siguiente(self):
        if self.pendientes.esta_vacia():
            print("Aviso: La cola está vacía, no hay solicitudes pendientes por atender.")
            return
        atendida = self.pendientes.desencolar()
        self.historial.apilar(atendida)
        print(f"Atendida y movida al historial: {atendida}")

    def consultar_pendientes(self):
        actual = self.pendientes.frente
        if actual is None:
            print("No hay solicitudes pendientes en este momento.")
            return
        print("\n--- SOLICITUDES PENDIENTES ---")
        while actual is not None:
            print(actual.data)
            actual = actual.next

    def consultar_ultima_atendida(self):
        cima = self.historial.consultar_cima()
        if cima is None:
            print("Aviso: El historial está vacío, aún no se ha atendido ninguna solicitud.")
        else:
            print(f"Última solicitud atendida (Cima de la pila): {cima}")