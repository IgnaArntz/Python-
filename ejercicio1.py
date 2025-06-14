#promedioNotas
sw=1
listaNotas = []

print("Presione 1 para ingresar sus notas: ")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción: "))

if(op ==1):
    while sw==1:
        try:
            print("--------------------------------")
            nota=int(input("Incorpore su nota, si desea salir, presione 0:"))
            if(nota !=0):
               listaNotas.append(nota)
               print(f"las listas de notas es: {listaNotas}")
               print(f"la cantidad de notas ingresadas es: {len(listaNotas)}")
               print(f"el promedio de notas es: {sum(listaNotas)/len(listaNotas)}")

            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")
else:
    print("Adiós")


