#leer un numero entero comprendido entre 1 y 7 e imprimir en pantalla los dias de semana

print("Ingrese número entre 1 al 7: ")
dia = int(input())

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado") 
elif dia == 7:
    print("Domingo")
else:
    print("Este número no corresponde a un dia de la semana")


