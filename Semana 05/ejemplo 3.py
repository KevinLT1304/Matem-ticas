#area y perimetro de un circulo
import math 

print("Ingrese radio:")
r = float(input())

a = math.pi*math.pow(r,2)
p = 2*math.pi*r

print("El area del círculo es:",a)
print("Y su perimetro es:",p)