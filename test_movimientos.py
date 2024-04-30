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








