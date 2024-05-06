"""
1. Pedir si es ingreso o gasto o salir
2. Si es ingreso
    2.1 Pedir concepto
    2.2 Pedir fecha
    2.3 Pedir cantidad
3. Si es gastos
    3.1 Pedir concepto
    3.2 Pedir fecha
    3.3 Pedir cantidad
    3.4 Pedir categoria
3.5 Si es salir salimos a 7
4. Instancir el movimiento (ingreso o gasto)
5. Almacenar el movimiento en una lista
6. volver a 1

7. Procesar la lista de movimientos para obtener total de ingresos, gastos y saldo final
"""
from kakebo import Ingreso, Gasto, CategoriaGastos
from datetime import date
listaMovimientos = []

def validarFecha(fecha):
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False

def esFloatPositivo(cantidad):
    try:
        cantidad = float(cantidad)
        return cantidad > 0
    except ValueError:
        return False

def esEntero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False
    
def esCategoriaValida(cadena):
    """
    1. comprobar que cadena es entero
    2. comprobar que cadena esta en el conjunto de values de categoriaGasto
    """
    if esEntero(cadena):
        entero = int(cadena)
        return entero in [categoria.value for categoria in CategoriaGastos]
    else: 
        return False

continuar = True
while continuar:
    tipo = input("Ingreso, Gasto o Salir (I/G/S): ").lower()

    while tipo not in ('i', 'g', 's'):
        print("Teclea I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()

    if tipo == 'i':
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha (YYYY-MM-DD): ") 
        while not validarFecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat(fecha)
        
        cantidad = input("Cantidad: ")
        while not esFloatPositivo(cantidad):
            print("Introduce un número positivo")
        cantidad = float(cantidad)

        listaMovimientos.append(Ingreso(concepto, fecha, cantidad))

    elif tipo == 'g':
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha (YYYY-MM-DD): ") 
        while not validarFecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat(fecha)

        cantidad = input("Cantidad: ")
        while not esFloatPositivo(cantidad):
            print("Introduce un número positivo")
        cantidad = float(cantidad)

        print("Lista de categoría de gastos: ")
        for categoria in CategoriaGastos:
            print(f"{categoria.value} - {categoria.name}")
        categoria_elegida = input("Elige el número de una de ellas: ")
        while not esCategoriaValida(categoria_elegida):
            print("Has elegido una opcióon incorrecta")
            print("Lista de categoría de gastos: ")
            for categoria in CategoriaGastos:
                print(f"{categoria.value} - {categoria.name}")
            categoria_elegida = input("Elige el número de una de ellas: ")
        categoria_elegida = CategoriaGastos(int(categoria_elegida))

        listaMovimientos.append(Gasto(concepto, fecha, cantidad, categoria_elegida))

    elif tipo == 's':
        continuar = False

print(listaMovimientos)