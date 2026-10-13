Sistema de Mesa de Ayuda

Proyecto en Python, la idea principal es armar las estructuras de Pila y Cola desde cero usando nodos y memoria dinámica, 
sin usar las listas ni funciones.

Archivos del proyecto

* nodo.py: El nodo básico con sus atributos privados y decoradores para enlazar los datos.
* pila.py: La Pila que usamos para el historial de atendidos.
* cola.py: La Cola para manejar pendientes que van llegando. Está para que funcione en tiempo constante.
* solicitud.py: Define los datos básicos de cada ticket (ID, nombre del usuario y la descripción del problema).
* MesaAyuda.py: El controlador que une la cola y la pila para que el sistema funcione.
* main.py: El menú interactivo para correr el programa en la consola.
* pruebas.py: Un script con las pruebas automáticas y los casos límite que pide el taller.

¿Cómo correrlo?

Abre tu terminal (Git Bash) en la carpeta del proyecto:

Para abrir el menú interactivo y probarlo manualmente:
bash
python main.py
