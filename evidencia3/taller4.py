# TALLER 4 
# NICOLAS ESPITIA VILLAMIL
# 06/07/2023

#LA FECHA CAGADA
import datetime
fecha = datetime.datetime.now()
print(f"\nHoy es el dia: {fecha}")

# PIDA TRES MEDIDDAS PARA UN TRIANGULO Y DIGA SI ES EQUI,ISO O ESC

print("\nIDENTIFICANDO TIPOS DE TRINAGULOS")
l1 = float(input(f"Primer lado del triangulo: "))
l2 = float(input(f"Segundo lado del triangulo: "))
l3 = float(input(f"Tercero lado del triangulo: "))

if l1 == l2 and l2 == l3 and l3 == l1:
    print("Es un triangulo equilatero")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")

# PIDA UN ANIMALACHO Y DIGA SI ES OSO, PERRO, GAT SI NO F

animal = input("\nIngrese un animal: ")

if animal == "PERRO":
    print(f"Es el mejor amigo del hombre,y muy fiel, {animal}")
elif animal == "OSO":
    print(f"Es animal que hiberna y es muy pesado {animal}")
elif animal == "GATO":
    print(f"Es un animal que caza ratones, {animal}")
else:
    print(f"Es un {animal}")

print("FIN")