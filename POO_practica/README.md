# PROGRAMACION ORIENTADA A OBJETOS PYTHON

### creacion de paquetes
se crea una carpeta y luego se crea un archivo como
--init--().py asi el interprete de python sabe que no es solo un archivo
sino un paquete.

### if "__main__"=="__main__"
explicaccion de la practiva uno y dos
La clase Producto y la clase Pedido se definen en el nivel superior.
Dentro del bloque if __name__ == "__main__":, se crean las instancias de Producto y Pedido y se llama a sus métodos correspondientes (total_pedido() y mostrar_productos()).
Esto garantiza que el código dentro del bloque if __name__ == "__main__": solo se ejecute si el archivo se ejecuta directamente como un script, no si se importa como un módulo.
en resumen evita que las lineas fuera de la clase o metodos se ejecuten si se llaman de manera externa
