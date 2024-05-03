from datetime import date

class Ingreso:
    def __init__(self, concepto, fecha, cantidad):
        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad
        self.__validar_tipos()

    def __validar_tipos(self): #al poner __ es para esconderlo el metodo y el atributo que sea de uso privado/interno, solo puede ser accedido desde dentro de la clase
        if not isinstance(self.concepto, str):
            raise TypeError("Concepto debe ser cadena de texto")
        if not isinstance(self.fecha, date):
            raise TypeError("Fecha debe ser de tipo date")
        if not (isinstance(self.cantidad, float) or isinstance(self.cantidad, int)):
            raise TypeError("La cantidad tiene que ser numérica")
        if not len(self.concepto) > 5:
            raise TypeError("Ingresa un nombre que sea mayor de 5 caracteres")
        if self.cantidad == 0:
            raise TypeError("Ingresa un número que sea mayor de 0")
        if self.fecha > date.today():
            raise TypeError("La fecha no puede ser posterior al día de hoy")