
class Ingreso:
    def __init__(self, concepto, fecha, cantidad):
        if not isinstance(concepto, str):
            raise TypeError("Concepto debe ser cadena de texto")

        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad
