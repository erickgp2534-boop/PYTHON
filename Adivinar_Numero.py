import random

aleatorio = random.randint(1,10)
intentos = 0
while True:
    try:
     print("===ADIVINA EL NUMERO===")
     numero = int(input("Ingrese el numero dentro de un rango de 1 a 10: "))
     intentos += 1
     if numero == aleatorio:
        print(f"Acertaste al numero: {aleatorio}")
        print(f"Lo hiciste en {intentos} intentos")
        break
     else:
        print(f"No acertaste al numero, intenta de nuevo")
    except ValueError:
       print("Tiene que ser un numero entero.")