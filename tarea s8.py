print("----VENTA DE UVA POR KILO----")
k = 5
print("---------KILO",k,"soles--------")
print("Tipos de uva:")
print("A (Moradas) y B (Verdes)")
print("Tamaño de uva:")
print("1 (grandes) y 2 (pequeñas)")
print("El pago depende del tipo y tamaño")
print("¿Qué tipo de uva desea?")
tipe = input()
print("¿Que tamaño desea?")
tam = float(input())

if tipe=="A" or tipe=="a" and tam==1:
    pf = k + 0.20
    print("El pago final es",pf,"soles")
elif tipe=="A" or tipe=="a" and tam==2:
    pf = k + 0.30
    print("El pago final es",pf,"soles")
elif tipe=="B" or tipe=="b" and tam==1:
    pf = k - 0.30
    print("El pago final es",pf,"soles")
elif tipe=="B" or tipe=="b" and tam==2:
    pf = k + 0.50
    print("El pago final es",pf,"soles")
else:
    print("Tipo de uva o tamaño incorrectos") 