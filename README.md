# Text Expander
# Manual de uso

Modulos necesarios:
- Pynput (Instalable desde Pip)
- Os (Pre-Instalado)

Funcionalidad:
- Se debe configurar una (o varias) claves de 3 letras para que luego sea reemplazada por un texto prestablecido

Como Funciona?
- Con Pynput recibe los inputs del teclado
- Se crea una lista de las teclas apretadas y se revisa si las ultimas 3 letras pertenecen a las claves seleccionadas
- Las claves son siempre de 3 letras y se deben agregar en el diccionario "database"
- En caso de querer cerrar el programa se debera tocar "qqq" para finalizarlo

Posibles Mejoras:
- Las claves no pueden contener numeros, incluirlos
- Cerrar el programa de una manera correcta y no forzando un error
- Optimizaciones de codigo y espacio
- Generacion de una interfaz para poder interactuar mas facilmente
- Convertirlo en un .exe
