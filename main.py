"""
1. pedir si es ingreso o gasto
2. Si es ingreso
    2.1 Pedir concepto
    2.2 Pedir fecha
    2.3 Pedir cantidad
3. Si es gasto
    3.1 Pedir concepto
    3.2 Pedir fecha
    3.3 Pedir cantidad
    3.4 Pedir categoría, mostrar las categorías
    3.5 Si es salir salimos a 7
4. Instanciar el movimiento (ingreso o gasto)
5. Almacenar el movimiento en una lista
6. Volver a 1

7. Procesar la lista de movimientos para obtener total de ingresos, gastos y saldo final.
"""
from kakebo import Ingreso, Gasto, CategoriaGastos
from datetime import date


listaMovimientos = [] #inicializamos lista a cero para meter todos los movimientos.
#validaciones
def validarFecha(fecha): #se encarga de que el formato sea correcto y que sea menos o igual a hoy, no valida el tipo.
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False

def imprimirMovimientos(): #muestra en pantalla todos los gasstos e ingresos introducidos por el usuario una vez que seleccionemos el tipo s (salir).
    print("Movimientos registrados:") #para que el usuario vea que el movimiento se ha registrado.
    for elemento in listaMovimientos:
        print(elemento)
    print("Fin de movimientos registrados")

def instanciarMovimiento(tipo, concepto, fecha, cantidad, categoria_elegida = ""): #le pasa al molde(clase) todos los datos para instanciar un movimiento (crear una instancia de un movimiento).
       
        if tipo == "i":
            movimiento = Ingreso(concepto, fecha, cantidad)
        if tipo == "g":
            movimiento = Gasto(concepto, fecha, cantidad, categoria_elegida)
        almacenarMovimiento(movimiento) #recibe el movimiento recien instanciado, y como almacenarMovimeinto(movimiento) es una función, se lleva el movimiento recien instaciado y lo pasa por ahí.Esto se hace para que todos estén registrados y disponibles al salir del proceso de crear nuevos movimientos.


def almacenarMovimiento(movimiento): #almacena los movimientos en la lista que tenemos definida arriba.
    listaMovimientos.append(movimiento)
    print("Movimeinto registrado correctamente")

continuar = True #iniciamos cotinuar en True para que se meta en el bucle general y cumplir con el punto 6 (volver a 1).
while continuar: 
    tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower() #pedimos al usuario que ingrese el tipo, lo forzamos para que lo pase a minúscula.

    while tipo not in ('i', 'g', 's'): #esto es para que si el tipo no está dentro de los valores que le damos, no salga del bucle hasta que nos de uno de los tipos permitidos ('i', 'g' o 's')
        print("Teclea una de las funciones I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()
        
        
    if tipo == "i": # si el tipo es igual a i.
        concepto = input("Concepto: ") #le pedimos el concepto y lo guardamos en una variable.
        while len(concepto) < 5: #este bucle es para que mínimo el concepto tenga 5 caracteres
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha: (YYYY-MM-DD): ") #le pedimos la fecha y lo guardamos en una variable.
        while not validarFecha(fecha): #comprobamos que el formato de la fecha sea el correcto. ¡importante el formato, no el tipo¡
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat(fecha) #aqui cambi el formato de fecha, de str a date, ya que en el input de la fecha devuelve una cadena 

        while True: #Iniciamos este bucle así ya que al iniciarlo asumimos que siempre es True, continuará ejecutandose sin parar hasta que cuando pase por el try y esto sea verdadero (la cantidad sea un float) hará el break y se parará.
            try: 
                cantidad = float(input("Intruduce la cantidad en números: ")) #le pedimos la cantidad y lo guardamos en una variable.
                
                if cantidad < 0: #si la cantidad es menor que 0, salta a la siguiente
                    cantidad = float(input("Introduce una cantidad que no sea negativa: "))
                if cantidad == 0: #pedimos que no sea 0
                    cantidad = float(input("Introduce una cantidad superior a 0, sin ser 0: "))
                if cantidad > 0: #si la cantidad es mayor que 0 pasa
                    break #break sale del bucle si la conversión fue ok
            except ValueError:
                print("Error: por favor introduce la cantidad con números válidos y no letras ni símbolos.")
        instanciarMovimiento(tipo, concepto, fecha, cantidad) #pasa los parametros recopilados a la función instanciar movimiento.

    if tipo == "g": #concepto fecha y cantidad funcionan igual que en tipo == "i"
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha: (YYYY-MM-DD): ")
        while not validarFecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat(fecha) #aqui cambi el formato de fecha, de str a date, ya que en el input de la fecha devuelve una cadena 
        while True:
            try: 
                cantidad = float(input("Intruduce la cantidad en números: "))
                if cantidad < 0: 
                    break
                elif cantidad == 0:
                    cantidad = float(input("Introduce una cantidad que no sea 0"))
                else:
                    cantidad *= -1
                    break 
            except ValueError:
                print("Error: Por favor introduce la cantidad con números válidos y no letras ni símbolos.")
        
        print("Lista de categorías de gastos: ")
        for categoria in CategoriaGastos: # este for imprime la class CategoriaGastos de forma que el usuario la entienda.
            print(f"{categoria.value} - {categoria.name}")
        while True: #este bucle comprueba que la categoría este dentro de los valores definidos dentro de la class CategoriaGastos
            eleccion_usuario = int(input("Introduce el número de la categoría de gastos: "))
            if eleccion_usuario in [categoria.value for categoria in CategoriaGastos]:
                categoria_elegida = CategoriaGastos(eleccion_usuario)
                break
            else:
                print("El número introducido no corresponde a ninguna categoría válida.")
        instanciarMovimiento(tipo, concepto, fecha, cantidad, categoria_elegida) #pasa los parametros recopilados a la función instanciar movimiento.

    if tipo == "s": #si el tipo es s, imprimimos los movimientos que se han realizado llamando a la función imprimirMovimientos.
        imprimirMovimientos() #ver información en la funcación imprimirMovimiento. Está arriba¡
        continuar = False #continuar en False para salir del bucle


    

 