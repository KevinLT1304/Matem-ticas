print("ingrese usuario")
usr = input()

print("Ingrese la contraseña")
pwd = input()

if usr == "admin" and pwd == "12345":
    msj = "Logueo exitoso"

else:
    msj = "intenta de nuevo"

print(msj)  