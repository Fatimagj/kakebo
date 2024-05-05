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


listaMovimientos = []
#validaciones
def validarFecha(fecha):
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False

def imprimirMovimientos():
    print("Movimientos registrados:")
    for elemento in listaMovimientos:
        print(elemento)
    print("Fin de movimientos registrados")

def instanciarMovimiento(tipo, concepto, fecha, cantidad, categoria_elegida = ""):
        fecha = date.fromisoformat(fecha)
        if tipo == "i":
            movimiento = Ingreso(concepto, fecha, cantidad)
        if tipo == "g":
            movimiento = Gasto(concepto, fecha, cantidad, categoria_elegida)
        almacenarMovimiento(movimiento)


def almacenarMovimiento(movimiento):
    listaMovimientos.append(movimiento)
    print("Movimeinto registrado correctamente")

continuar = True
while continuar:
    tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()

    while tipo not in ('i', 'g', 's'):
        print("Teclea una de las funciones I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()
        
        
    if tipo == "i":
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha: (YYYY-MM-DD): ")
        while not validarFecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")

        while True:
            try: 
                cantidad = float(input("Intruduce la cantidad en números: "))
                break # sale del bucle si la conversión fue ok
            except ValueError:
                print("Error: por favor introduce la cantidad con números válidos y no letras ni símbolos.")
        instanciarMovimiento(tipo, concepto, fecha, cantidad)

    if tipo == "g":
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha: (YYYY-MM-DD): ")
        while not validarFecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")

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
        
        for categoria in CategoriaGastos: #imprime la lista de gastos
            print(f"{categoria.value} - {categoria.name}")
        while True:
            eleccion_usuario = int(input("Introduce el número de la categoría de gastos: "))
            if eleccion_usuario in [categoria.value for categoria in CategoriaGastos]:
                categoria_elegida = CategoriaGastos(eleccion_usuario)
                break
            else:
                print("El número introducido no corresponde a ninguna categoría válida.")
        instanciarMovimiento(tipo, concepto, fecha, cantidad, categoria_elegida)

    if tipo == "s":
        imprimirMovimientos()
        continuar = False


    

 