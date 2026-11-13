'''
Una calculadora que pide dos números al usuario, 
le pregunta qué operación quiere hacer 
(suma, resta, multiplicación, división) y muestra el resultado. Parece simple, pero te enseña input(), if/elif/else, conversión de tipos y manejo de errores básico (dividir entre cero).

Conceptos que practicas
input()
if/elif/else
float()
try/except
Qué debe hacer
Pide dos números con input() y los convierte a float
Un menú con las 4 operaciones básicas
Si elige división y el segundo número es 0, muestra error en lugar de caerse
Al final pregunta si quiere hacer otro cálculo (ciclo while)
'''

while True:
    try:
     print("===CALCULADORA SIMPLE===")
     print("1. SUMA")
     print("2. RESTA")
     print("3. MULTIPLICACION")
     print("4. DIVISION")
     print("5. SALIR")
     opcion = int(input("Elige la opcion que desea: "))
     num1 = float(input("Ingrese el primer numero: "))
     num2 = float(input("Ingrese el segundo numero: "))
     if opcion == 1:
       suma = num1 + num2
       print(f"La suma de los dos numeros es: {suma}")
     elif opcion == 2:
       resta = num1 - num2
       print(f"La resta de los dos numeros es: {resta}")
     elif opcion == 3:
       multiplicacion = num1 * num2
       print(f"La multiplicacion de los dos numeros es: {multiplicacion}")
     elif opcion == 4:
       try:
         division = num1 / num2
         print(f"La division de los dos numeros es: {division}")
       except ZeroDivisionError:
         print("Error al dividir por cero '0'")
     elif opcion == 5:
       print("Usted ah decidido Salir del programa Adios...")
       break
     else:
       print("Esta opcion no esta en la calculadora, por favor eliga otra.")
    except ValueError:
     print("Tienes que poner un numero, no otro tipo de dato")