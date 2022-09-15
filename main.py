import time

print("Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")


nombre = input("¿Ingresa tu nombre?")
puntaje = 0
TOTAL = 0
RED = '\033[31m'
GREEN = '\033[32m'
AZUL = '\033[34m'
RESET = '\033[39m'
time.sleep(2)
print("\nHola ", nombre,"Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")
print(AZUL+nombre +" Tienes", puntaje, "puntos"+RESET)  


print("\n1. ¿Cual no esta en la lista de sistemas operativos?\n")
print("a) Linux ")
print("b) Windows")
print("c) Mac OS")
print("d) Ritchie")
respuesta_1 = input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
if respuesta_1 == "d":
    puntaje += 10
    print(GREEN+"muy bien"+RESET)
else:
    puntaje -= 10
    print(RED+"incorrecta"+RESET)
        
print("\n2. ¿Cuál de los siguientes es el Sistema Operativo que no maneja Interfaz Gráfica?\n")
print("a) Windows 2000 ")
print("b) Mac OS")
print("c) Unix")
print("d) Windows XP")
respuesta_1 = input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ") 
if respuesta_1 == "c":
    puntaje += 10
    print(GREEN+"muy bien"+RESET)
else:
    puntaje-=10
    print(RED+"incorrecta"+RESET)
    

print("\n3. ¿Cuál de las siguientes es una función del Sistema Operativo?\n")
print("a) Administrar los recursos de la computadora ")
print("b) Organizar la información que se almacena en la computadora")
print("c) Ser una interfaz entre la computadora y el usuario")
print("d) Todas las anteriores")
respuesta_1 = input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ") 
if respuesta_1 == "d":
    puntaje += 10
    print(GREEN+"muy bien"+RESET)
else:
    puntaje-=10
    print(RED+"incorrecta"+RESET)

print("\n4. ¿Qué es un Sistema Operativo?\n")
print("a) Programas que inicializan a la computadora. ")
print("b) Conjunto de instrucciones que ayuda al usuario en la realización de un tarea.")
print("c) Conjunto de programas que administran las tareas que son ejecutadas concurrentemente en la computadora")
print("d) Todas las anteriores")
respuesta_1 = input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ") 
if respuesta_1 == "d":
    puntaje += 10
    print(GREEN+"muy bien"+RESET)
else:
    puntaje-=10
    print(RED+"incorrecta"+RESET)

print("\n5. Mencione los requerimientos para instalar Windows XP:\n")
print("a) Computadora y teclado ")
print("b) Procesador PII 166 MHz, 64 MB RAM")
print("c) Procesador PIII 233 MHz, 128 MB RAM")
print("d) Ninguna de las anteriores")
respuesta_1 = input("\nTu respuesta: ")
while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ") 
if respuesta_1 == "d":
    puntaje += 10
    print(GREEN+"muy bien"+RESET)
else:
    puntaje-=10
    print(RED+"incorrecta"+RESET)

if puntaje <=0:
  print ("Gracias", nombre, "por jugar mi trivia, alcanzaste", TOTAL, "puntos")  
else:
  print ("Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos") 

