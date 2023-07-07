# Taller 2
# Nicolas Espitia Villamil
# 30/06/2023

#Fechas

import datetime
import math

hoy = datetime.datetime.today()
print(f"\nHoy es {hoy}")


#Variables

num1 = input("Ingresa primer numero: ")
num2 = input("Ingresa segundo numero: ")
num3 = input("Ingresa tercer numero: ")

arr = [int(num1), int(num2), int(num3)]


#Operaciones con el arreglo

print(f"""
    El numero mayor es: {max(arr)} 
    El numero menor es: {min(arr)}
    La suma del arreglo es: {sum(arr)}
""")


#Redondeando un numero

numR = input("Ingresa un numero que desees redondear: ")
print(f"El numero {numR} redondeado es: {round(float(numR))}")


#Modificanco cadenas de txt

cadena = input("Ingresa un texto que desees modificar: ")
print(f"""
    En mayusculas: {cadena.upper()}
    En minusculas: {cadena.lower()}
    Primera en mayus: {cadena.capitalize()}
    Cada palabra comienza en mayuss: {cadena.title()}  
    Conteo de caracteres: {len(cadena)}
""")

print("FIN :D")