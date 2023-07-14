# TALLER 5 PYTHON
# NICOLAS ESPITIA VILLAMIL
# 13/07/2023

#FECHA DE HOY
import datetime
fecha = datetime.datetime.today()
print(f"\nHola la fecha de hoy es {fecha}")

#5 CICLOS CON FOR
print("\nA continuación realizaremos 5 bucles con la sentencia FOR")


#PIDE DOS NUMEROS
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))


#PRIMERO PARA LLEGAR HASTA ESE NUMERO
print("\nAhora iremos desde 1 hasta ese el primer numero que ingresaste :)")

for i in range(num1):
    print(f"    {i+1}")
    

#SEGUNDO PARA EL NUM1 HASTA EL NUM2
print("\nAhora iremos del primer numero al segundo numero ingresado")
for i in range(num1, num2):
    print(f"    {i}")


#TERCERO DEL PRIMERO AL SEGUNDO DE DOS EN DOS
print("\nIremos igual pero ahora de dos en dos")
for i in range(num1, num2, 2):
    print(f"    {i}")

#CUARTO PIDA EL NOMBRE DE UNA EMPRESA Y PASELO A MINUSCULAS, PARA LUEGO MOSTRARLO CARACER POR CARACTER 

nombreEmp = input("\nIngrese el nombre de una empresa: ")

print("\nEn minusculas: ")
print(nombreEmp.lower())

print("\nAhora imprimiremos letra por letra :)")

for carac in nombreEmp:
    print(carac)