#listaSuper
sw = 1
listaSuper = []
valorSuper = []

print("Presione 1 para ingresar los productos del súper")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción "))
if(op == 1):
    while sw==1:
        try:
            print("----------------------------------------------------------")
            producto=input("Incorpore su producto, para salir, presione 0: ")
            if(producto != "0"):
                listaSuper.append(producto)
                ValorProducto = int(input(f"Incorporee el valor del {producto} "))
                valorSuper.append(ValorProducto)
                
                print("-----DETALLE BOLETA-----")
                print(f"Sus productos comprados son: {listaSuper}")
                print(f"La cantidad de productos comprados es: {len(listaSuper)}")
                print(f"la suma total es: {sum(valorSuper)}")
            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erroneo")
else:
    print("Adiós")
