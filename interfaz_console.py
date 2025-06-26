from controlador import ControladorSalario

def main():
    archivo = "PlanillaCalculo.xlsx"
    controlador = ControladorSalario(archivo)

    try:
        mes = input("Ingrese el número de mes a calcular (por ejemplo 04 para abril): ").zfill(2)
        nombre = input("Ingrese el nombre del trabajador: ")

        print("\nSeleccione el tipo de cálculo:")
        print("1. Por cantidad de palabras")
        print("2. Por tiempo trabajado")
        opcion = input("Ingrese su opción (1 o 2): ")

        tipo = "palabra" if opcion == "1" else "hora"

        salario = controlador.ejecutar_calculo(mes=mes, tipo=tipo, nombre_trabajador=nombre)
        print(f"\nSalario mensual estimado: {salario:.2f} guaraníes")

    except Exception as e:
        print(f"\nError: {e}")
