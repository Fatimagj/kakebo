from datetime import date
from enum import Enum

class Ingreso:
    def __init__(self, concepto, fecha, cantidad):
        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad
        self.__validar_tipos()
        self.validar_inputs()

    def __validar_tipos(self): #al poner __ es para esconderlo el metodo y el atributo que sea de uso privado/interno, solo puede ser accedido desde dentro de la clase
        if not isinstance(self.concepto, str):
            raise TypeError("Concepto debe ser cadena de texto")
        if not isinstance(self.fecha, date):
            raise TypeError("Fecha debe ser de tipo date")
        if not (isinstance(self.cantidad, float) or isinstance(self.cantidad, int)):
            raise TypeError("La cantidad tiene que ser numérica")
    def validar_inputs(self): 
        if not len(self.concepto) > 5:
            raise TypeError("Ingresa un nombre que sea mayor de 5 caracteres")
        if self.cantidad == 0:
            raise TypeError("Ingresa un número que sea mayor de 0")
        if self.fecha > date.today():
            raise TypeError("La fecha no puede ser posterior al día de hoy")
    def __repr__(self): #es un elemento magico, que nos transforma lo que nos da de donde esta y nos lo representa más claramente para que sepamos donde esta el error. Esto se tiene que crearen cada clase de forma distinta, no se hereda
        return f"Ingreso: {self.fecha} {self.concepto} {self.cantidad:.2f}"

class Gasto(Ingreso):
    def __init__(self, concepto, fecha, cantidad, categoria):
        super().__init__(concepto, fecha, cantidad) #es para heredar de la madre que es ingresos, pass es para coger de la hija
        self.categoria = categoria
        
        if not isinstance(self.categoria, CategoriaGastos):
            raise TypeError("Categoría debe estar entre los números 1-4.")
    def __repr__(self): #aqui se ve que se tiene que hacer en la otra clase
        return f"Gasto ({self.categoria.name}): {self.fecha} {self.concepto} {self.cantidad:.2f}"

class CategoriaGastos(Enum):
    NECESIDAD = 1
    CULTURA = 2
    OCIO_VICIO = 3
    EXTRAS = 4
