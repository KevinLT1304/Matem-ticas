#ingresar el sueldo de un empleado y de acuerdo a su categoria se le dara una bonificacion
#si la categoria es "a" se le dara un bono del 5%
#si la categoria es "b" se le dara un bono del 10%
#si la categoria es "c" se le dara un bono del 15%
#calcule la bonificacion y el sueldo neto


print("--------Cuadro de bonificacion-------------")
print("categoria es "'a'" se le dara un bono del 5%")
print("categoria es ""b"" se le dara un bono del 10%")
print("categoria es ""c"" se le dara un bono del 15%")

print("Ingrese salario")
salario = float(input())

print("Ingrese categoria")
cat = str(input())


#bn1 = (salario*0.05)
#bn2 = (salario*0.10)
#bn3 = (salario*0.15)

#sueldoneto1 = salario+bn1 
#sueldoneto2 = salario+bn2 
#sueldoneto3 = salario+bn3 

#if cat=="a":
 #   print("Su categoria es ""a"", la bonificacion es",bn1," y su sueldo neto es ",sueldoneto1)
#elif cat=="b":
  #      print("Su categoria es ""b"", la bonificacion es",bn2,"y su sueldo neto es ",sueldoneto2)
#elif cat=="c":
 #       print("Su categoria es ""c"", la bonificacion es",bn3,"y su sueldo neto es ",sueldoneto3)
#else:
 #   print("No hay bonificacion para este sueldo")


if cat=="a" or cat=="A":
    bonif = 0.05*salario
elif cat=="b" or cat=="B":
         bonif = 0.10*salario
elif cat=="c" or cat=="C":
         bonif = 0.15*salario
else:
     bonif = 0*salario

sueldoneto = salario + bonif
print("La bonificacion es",bonif)
print("Su sueldo neto es",sueldoneto)        