print("Calcular el volumen de una esfera")
print("---------------------------------")
print("Ingrese el Diámetro:")
d = float(input())
r = d/2
v = 4/3*3.14*r**3
print("---------------")
print("El volumen es: ",v)

print("Redondeando sería: ", round(v,1))