class Solicitud:
    def __init__(self, id_solicitud, usuario, descripcion):
        self.id_solicitud = id_solicitud
        self.usuario = usuario
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id_solicitud} | Usuario: {self.usuario} | Descripcion: {self.descripcion}"