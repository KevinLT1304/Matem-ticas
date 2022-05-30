print("Tarifa por horas")
print("----------------")
print("8h = 80 soles")
print("7h = 70 soles")
print("5h = 45 soles")
print("3h = 25 soles")
horas3 = 25
horas5 = 45
horas7 = 70
horas8 = 80

print("-----------------------------")
print("¿Cuántas horas ha trabajado?: ")
num = int(input())
print("-----------------------------")

if num ==3:
    print("Su salario bruto es de: ",horas3,"soles")
    sneto = (horas3*0.1)+horas3
    print("Su salario neto es de: ",sneto, "soles")

elif num ==5:
    print("Su salario bruto es de: ",horas5,"soles")
    sneto = (horas5*0.1)+horas5
    print("Su salario neto es de: ",sneto, "soles")

elif num ==7:
    print("Su salario bruto es de: ",horas7,"soles")
    sneto = (horas7*0.1)+horas7
    print("Su salario neto es de: ",sneto, "soles")

elif num ==8:
    print("Su salario bruto es de: ",horas8,"soles")
    sneto = (horas8*0.1)+horas8
    print("Su salario neto es de: ",sneto, "soles")

else:
    print("-------------------------------------------------------")
    print("Ingrese una hora establecida por la tarifa. Por favor:)")         