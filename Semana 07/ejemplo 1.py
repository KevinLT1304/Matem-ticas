#dado un número determinar si es positivo o negativo
print("Ingrese un numero")
numero = int(input())

if numero>0:
    rpta="El número es positivo"
elif numero==0:
    rpta="El número es cero"
else:
    rpta="El número es negativo"

print(rpta)    