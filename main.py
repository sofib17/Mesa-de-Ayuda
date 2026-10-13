from mesa_ayuda import MesaAyuda

def ejecutar_menu():
    sistema = MesaAyuda()
    opcion = ""

    while opcion != "6":
        print("\n=== MESA DE AYUDA - SOPORTE TÉCNICO ===")
        print("1. Registrar una solicitud")
        print("2. Atender la siguiente solicitud")
        print("3. Consultar solicitudes pendientes")
        print("4. Consultar la última solicitud atendida")
        print("5. Mostrar estado general / Pruebas")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            id_s = input("Ingrese ID único: ")
            usuario = input("Nombre del usuario: ")
            desc = input("Descripción del problema: ")
            sistema.registrar_solicitud(id_s, usuario, desc)
        elif opcion == "2":
            sistema.atender_siguiente()
        elif opcion == "3":
            sistema.consultar_pendientes()
        elif opcion == "4":
            sistema.consultar_ultima_atendida()
        elif opcion == "5":
            print("Sistema operando correctamente bajo estructuras de Pila y Cola.")
        elif opcion == "6":
            print("Saliendo de la aplicación de Mesa de Ayuda...")
        else:
            print("Opción inválida, por favor intente de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()