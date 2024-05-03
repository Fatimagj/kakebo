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

def validarFecha(fecha):
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False
    
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

