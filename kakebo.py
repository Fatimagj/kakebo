from datetime import date

class Ingreso:
    def __init__(self, concepto, fecha, cantidad):
        if not isinstance(concepto, str):
            raise TypeError("Concepto debe ser cadena de texto")
        if not isinstance(fecha, date):
            raise TypeError("Fecha debe ser de tipo date")
        if not (isinstance(cantidad, float) or isinstance(cantidad, int)):
            raise TypeError("La cantidad tiene que ser numérica")

        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad
