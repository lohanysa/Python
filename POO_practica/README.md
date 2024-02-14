# PROGRAMACION ORIENTADA A OBJETOS PYTHON

### String
Qué son los métodos string en Python
En Python, los métodos de cadenas (string methods) son funciones incorporadas que se utilizan para manipular y trabajar con cadenas de texto. Las cadenas en Python son objetos inmutables, lo que significa que no se pueden modificar directamente, pero los métodos de cadenas proporcionan diversas operaciones y transformaciones que permiten manipularlas.

A continuación puedes consultar los métodos string en Python:

Método	Descripción
- capitalize():	Convierte el primer carácter a mayúsculas
- casefold():	Convierte cadena en minúsculas
- center():	Devuelve una cadena centrada
- count():	Devuelve el número de veces que aparece un valor especificado en una cadena
- encode():	Devuelve una versión codificada de la cadena.
- endswith():	Devuelve verdadero si la cadena termina con el valor especificado
- expandtabs():	Establece el tamaño de pestaña de la cadena.
- find():	Busca en la cadena un valor específico y devuelve la posición donde se encontró
- format():	Formatea valores especificados en una cadena
- format_map():	Formatea valores especificados en una cadena
- index():	Busca en la cadena un valor específico y devuelve la posición donde se encontró
- isalnum():	Devuelve True si todos los caracteres de la cadena son alfanuméricos
- isalpha():	Devuelve True si todos los caracteres de la cadena están en el alfabeto
- isascii():	Devuelve True si todos los caracteres de la cadena son caracteres ASCII
- isdecimal():	Devuelve True si todos los caracteres de la cadena son decimales
- isdigit():	Devuelve True si todos los caracteres de la cadena son dígitos
- isidentifier():	Devuelve True si la cadena es un identificador
- islower():	Devuelve True si todos los caracteres de la cadena están en minúsculas
- isnumeric():	Devuelve True si todos los caracteres de la cadena son numéricos
- isprintable():	Devuelve True si todos los caracteres de la cadena son imprimibles
- isspace():	Devuelve True si todos los caracteres de la cadena son espacios en blanco
- istitle():	Devuelve True si la cadena sigue las reglas de un título
- isupper():	Devuelve True si todos los caracteres de la cadena están en mayúsculas
- join():	Convierte los elementos de un iterable en una cadena
- ljust():	Devuelve una versión justificada a la izquierda de la cadena.
- lower():	Convierte una cadena en minúsculas
- lstrip():	Devuelve una versión recortada a la izquierda de la cadena.
- maketrans():	Devuelve una tabla de traducción para ser utilizada en las traducciones.
- partition():	Devuelve una tupla donde la cadena se divide en tres partes
- replace():	Devuelve una cadena donde un valor especificado se reemplaza con un valor especificado
- rfind():	Busca en la cadena un valor específico y devuelve la última posición donde se encontró
- rindex():	Busca en la cadena un valor específico y devuelve la última posición donde se encontró
- rjust():	Devuelve una versión justificada a la derecha de la cadena.
- rpartition():	Devuelve una tupla donde la cadena se divide en tres partes
- rsplit():	Divide la cadena en el separador especificado y devuelve una lista
- rstrip():	Devuelve una versión recortada a la derecha de la cadena.
- split():	Divide la cadena en el separador especificado y devuelve una lista
- splitlines():	Divide la cadena en los saltos de línea y devuelve una lista
- startswith():	Devuelve verdadero si la cadena comienza con el valor especificado
- strip():	Devuelve una versión recortada de la cadena.
- swapcase():	Intercambia mayúsculas y minúsculas y viceversa
- title():	Convierte el primer carácter de cada palabra a mayúsculas
- translate():	Devuelve una cadena traducida
- upper():	Convierte una cadena en mayúsculas
- zfill():	Rellena la cadena con un número especificado de valores 0 al principio

### cast 
Cast en Python
Cast» o casting en python, es la operación de convertir un tipo de dato a otro tipo de dato distinto. Python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de una variable antes de usarla, y Python realiza automáticamente algunas conversiones implícitas cuando es necesario. Sin embargo, en algunas ocasiones, es necesario realizar conversiones explícitas para adecuar los datos a ciertas operaciones específicas o para garantizar que el resultado sea el esperado.

Tipos de conversiones o casting en Python:

- Cast a entero (int): int(valor)
- Cast a punto flotante (float): float(valor)
- Cast a cadena (str): str(valor)
- Cast a lista (list): list(secuencia)
- Cast a tupla (tuple): tuple(secuencia)
- Cast a conjunto (set): set(secuencia)
- Cast a diccionario (dict): dict(lista_de_pares_clave_valor)
- Cast a booleano (bool): bool(valor)

### creacion de paquetes
se crea una carpeta y luego se crea un archivo como
--init--().py asi el interprete de python sabe que no es solo un archivo
sino un paquete.

### if "__main__"=="__main__"
explicaccion de la practiva uno y dos
La clase Producto y la clase Pedido se definen en el nivel superior.
Dentro del bloque if __name__ == "__main__": se crean las instancias de Producto y Pedido y se llama a sus métodos correspondientes (total_pedido() y mostrar_productos()).
Esto garantiza que el código dentro del bloque if __name__ == "__main__": solo se ejecute si el archivo se ejecuta directamente como un script, no si se importa como un módulo.
en resumen evita que las lineas fuera de la clase o metodos se ejecuten si se llaman de manera externa

### Lista informacion adicional
Este ejemplo muestra diferentes formas de crear listas en Python:

- Crear una lista vacía en Python: mi_lista_vacia = [].
- Crear una lista con elementos en Pyhton: frutas = [«manzana», «banana», «cereza», «uva»].
- Crear una lista con diferentes tipos de datos en Python: mi_lista_mixta = [1, «Hola», True, 3.14].
- Crear una lista de números del 1 al 5 usando una comprensión de lista en Python: numeros = [x for x in range(1, 6)].
- Crear una lista de cadenas utilizando el método split() en una cadena en Python: palabras = mi_cadena.split().
- Crear una lista de números pares utilizando un bucle for en Python: numeros_pares = [i for i in range(2, 11, 2)].
- Crear una lista de listas en Python(una lista de listas de números): lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

__RECORDATORIO__
En Python, una instancia es un objeto creado a partir de una clase, que contiene sus propios atributos y métodos. 
Una clase es como un molde o plantilla para crear objetos con propiedades y comportamientos específicos. 
Cuando creas una instancia de una clase, estás creando un objeto único con sus propios valores de atributos y métodos heredados de la clase.