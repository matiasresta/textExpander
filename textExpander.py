#MANUAL DE USO
"""
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
"""

from pynput.keyboard import Listener, Key, Controller
import os

controller = Controller()
database = {
    "adq": "HOLA ESTE ES UN TRIAL",
    "teq": "Este es la segunda prueba"
}

try:
    os.remove(os.path.join(os.getcwd(), "text.txt"))
except:
    pass

def writeToFile(key):

    key = str(key)
    if key == "Key.space":
            key = " "
    if len(key) == 3:
        key = key[1]
        
    with open("text.txt", "a") as textFile:
        if len(key) == 1:
            print(key)
            textFile.write(',' + key)
            if key == "Key.space":
                textFile.close()

    with open("text.txt", "r") as textFile:
            data = textFile.read()[1:].split(",")
            textLen = len(data)
            comm = "".join(data[-3:])

            if comm in database:
                controller.release(Key.backspace); controller.press(Key.backspace)
                controller.release(Key.backspace); controller.press(Key.backspace)
                controller.release(Key.backspace); controller.press(Key.backspace)
                controller.type(database[comm])
                textFile.close()
                os.remove(os.path.join(os.getcwd(), "text.txt"))

            if textLen > 3000:
                textFile.close()
                os.remove(os.path.join(os.getcwd(), "text.txt"))

            if comm == "qqq":
                textFile.close()
                os.remove(os.path.join(os.getcwd(), "text.txt"))
                print(selfSuicide) #Forma no elegante de Terminar el programa, Fuerza un error

            print(data)
            print(len(data))

with Listener(on_press=writeToFile) as l:
    l.join()
