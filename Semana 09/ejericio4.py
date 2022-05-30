def ajuste_precio(tipe, tam, k):

    if (tipe=="A" or tipe=="a") and tam==1:
        pf = k + 0.20

    elif (tipe=="A" or tipe=="a") and tam==2:
        pf = k + 0.30
    
    elif (tipe=="B" or tipe=="b") and tam==1:
        pf = k - 0.30

    elif (tipe=="B" or tipe=="b") and tam==2:
        pf = k + 0.50
    else:
        pf = k    
    return pf    

nuevoprecio = ajuste_precio("A",1,1)
print(nuevoprecio)    