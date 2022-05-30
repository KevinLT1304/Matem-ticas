#entrada
#print("Ingrese primer numero:")
#n1 = float(input())

#   n2 = float(input())
#proceso

#resultado = ('El producto es'),(n1*n2)
#if n1!=n2:
 #   resultado = n1+n2;

  #  resultado =("Son diferentes!. Entonces la suma es: ",resultado)
#salida

#print(resultado)

print("Ingrese primer numero:")
n1 = float(input())
n2 = float(input())
#proceso
suma = n1+n2
producto = n1*n2

if n1!=n2:
    mensaje = "La suma es",suma

if n1==n2:
    mensaje = "EL producto es", producto

print(mensaje)