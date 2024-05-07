f = open("./data/movimientos.dat", "r")
cabecera = f.readline()
print(cabecera)
for linea in f:
    print(linea, end="")
    print("y ahora separado")
    print(linea.split(","))
f.close()
