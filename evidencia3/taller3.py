# TALLER 3 PYTHON
# NICOLAS ESPITIA VILLAMIL
# 06/07/2023

#Fecha

import datetime
hoy = datetime.datetime.now()
print(f"\nHoy es {hoy}")


#Valide el dato mayor

a = input("\nIngrese el primer numero: ")
b = input("Ingrese el segundo numero: ")


#Condicional que valida

if(int(a) > int (b)):
    print(f"a({a}) es mayor que b({b})")
elif(int(b) > int(a)):
    print(f"b({b}) es mayor que a({a})")
else:
    print("Los dos numeros son iguales")


#Validacion de cursos

cur1 = "Requerimientos"
cur2 = "Algoritmos"

print(f"\nEl curso 1 es: {cur1}")
print(f"El curso 2 es: {cur2}")

if(cur1 == "Requerimientos" and cur2 == "Algoritmos"):
    print("Estas estudiando programacion")
else:
    print("No estas estudiando programacion")

#Solicita y valida la oracion

oracion = input("\nIngrese una oracion: ")
print(f"La oracion en mayusculas: {oracion.upper()}")

print(f"La longitud de la oracion es de: {len(oracion)} caracteres")

if(len(oracion) > 10):
    print("La oracion tiene mas de 10 caracteres")
else:
    print("La oracion tiene menos de 10 caracteres")

print("\nFIN")