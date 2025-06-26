from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('salario, es_eligible_bono, Nombre, Monto')

es_eligible_bono(Nombre) <= (salario[Nombre] > 4000000)

def evaluar_bono(nombre, monto):
    salario[nombre] = monto
    resultado = es_eligible_bono(nombre)
    return bool(resultado)
