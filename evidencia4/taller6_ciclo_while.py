# TALLER 6 CICLO WHILE
# NICOLAS ESPITIA VILLAMIL
# 14/07/2023

import datetime

#FECHA
fecha = datetime.datetime.today()
print(f"\nHoy es: {fecha}")

#6 CICLOS WHILE
print("\nImprimiremos 6 ciclos while a continuación")

#PIDA UN NUM
numero = int(input("\nIngrese un numero mayor a 1 y llegamos hasta el: "))

#SI ES MAYO A 1 LLEGUE HASTA EL NUM
i = 1 
while i <= numero:
    print(i)
    i += 1

#UN ADIVINADOR DE NUMERO Y UN CONTADOR DE CUANTOS INTENTOS HIZO
ocultoNum = int(7)
contador = 1
i = 1


intentoNum = int(input("\nQué numero esta oculto?: "))

while intentoNum != ocultoNum:
    print("Este no es el numero oculto :'(")
    intentoNum = int(input("Qué numero esta oculto?: "))
    contador += 1
print(f"Muy bien has acertado en el intento #{contador}")


#PIDA UN NOMBRE DE ALGUIEN, PASE A MAYUS, IMPRIMA POR CARACTER CON FOR HASTA QUE VEA LA A

amistad = input("\nIngrese el nombre de un amig@ y lo escribiré a menos que tenga una A: ").upper()

for letra in amistad:
    print(letra)

    if letra == "A":
        break
print("\t\nFIN")