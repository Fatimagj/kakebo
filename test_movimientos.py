from datetime import date
from kakebo import Ingreso
import pytest

def test_instanciar_ingreso():
    movimiento = Ingreso("Loteria del niño, premio", date(2024, 1, 5), 1000)
    
    assert movimiento.concepto == "Loteria del niño, premio"
    assert movimiento.fecha == date(2024, 1, 5)
    assert movimiento.cantidad == 1000

def test_ingreso_concepto_debe_ser_string():
    with pytest.raises(TypeError):
        movimiento = Ingreso(19, date(2024, 1, 5), 1000) 

def test_ingreso_fecha_typeError():
    with pytest.raises(TypeError):
        movimiento = Ingreso("Loteria del niño, premio", "1 de enero del 2024", 1000) 

def test_ingreso_cantidad_typeError():
    with pytest.raises(TypeError):
        movimiento = Ingreso("Loteria del niño, premio", date(2024, 1, 5), "0") 
    movimiento = Ingreso("Loteria del niño, premio", date(2024, 1, 5), 1000) 
    movimiento = Ingreso("Loteria del niño, premio", date(2024, 1, 5), 1000.1) 

# test que la cantidad no sea cero
# test que como minimo el concepto tieneque tener una longitud superior a 5 caracteres. El concepto debe tener una longitud mayor de 5
# test que la fecha no puede ser posterior a fecha de creación del ingreso. menor o igual a hoy, no se admitenn movimientos futuros

