# TALLER 1
# NICOLAS ESPITIA VILLAMIL
# FECHA: 30/06/2023

#Importamos la libreria de fechas
import datetime


#Declaramos e imprimimos la variable del día actual
hoy = datetime.datetime.today()
print(f"\nHoy es el dia {hoy}")


#realizamos operaciones matematics basicas
num1 = int(input("Ingresa un numero aqui: "))
num2 = int(input("Ingresa un segundo numero aqui: "))


suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = float(num1 / num2)


print(f"""
    La suma de estos numeros es de: {suma}
    La resta de estos numeros es de: {resta}
    La multiplicaion de estos numeros es de: {multiplicacion}
    La division de estos numeros es de {round(division, 2)}
""")