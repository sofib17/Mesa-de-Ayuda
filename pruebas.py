from mesaAyuda import MesaAyuda

def ejecutar_pruebas():
   
    print("   INICIANDO PRUEBAS DE ACEPTACIÓN")
    
    sistema = MesaAyuda()
    
    # 1. Probar consultar el historial antes de atender solicitudes (Caso límite)
    print("\n[Prueba 1] Consultar última atendida con pila vacía:")
    sistema.consultar_ultima_atendida()
    
    # 2. Registrar tres solicitudes identificadas como A, B y C en ese orden
    print("\n[Prueba 2] Registrando solicitudes A, B y C:")
    sistema.registrar_solicitud("101", "Usuario A", "Falla de red")
    sistema.registrar_solicitud("102", "Usuario B", "Error de aplicacion")
    sistema.registrar_solicitud("103", "Usuario C", "Impresora rota")
    
    # 3. Comprobar que la cola conserva el orden A - B - C
    print("\n[Prueba 3] Consultando solicitudes pendientes (Orden esperado: A, luego B, luego C):")
    sistema.consultar_pendientes()
    
    # 4. Atender dos solicitudes (Debe atender a A y luego a B)
    print("\n[Prueba 4] Atendiendo las dos primeras solicitudes:")
    sistema.atender_siguiente()
    sistema.atender_siguiente()
    
    # 5. Comprobar que la cima de la pila muestra a B como la última solicitud atendida
    print("\n[Prueba 5] Verificando la cima del historial (Debe ser la solicitud B):")
    sistema.consultar_ultima_atendida()
    
    # 6. Atender la última solicitud restante (C)
    print("\n[Prueba 6] Atendiendo la última solicitud (C):")
    sistema.atender_siguiente()
    
    # 7. Verificar el comportamiento del sistema cuando la cola queda vacía (Caso límite)
    print("\n[Prueba 7] Intentando atender cuando la cola ya está vacía:")
    sistema.atender_siguiente()
    
    print("   PRUEBAS FINALIZADAS CON ÉXITO")

if __name__ == "__main__":
    ejecutar_pruebas()
