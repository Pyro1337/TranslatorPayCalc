from datos import GestorDatos
from estrategias import CalculoPorPalabra, CalculoPorHora
from modelos import Trabajador
from persistencia import guardar_resultado_salario, cargar_resultado_salario

class ControladorSalario:
    def __init__(self, archivo_excel: str):
        self.datos = GestorDatos(archivo_excel)

    def ejecutar_calculo(self, mes: str, tipo: str, nombre_trabajador: str) -> float:
        # Verificar si ya hay resultado guardado previamente
        resultado_guardado = cargar_resultado_salario(nombre_trabajador, mes, tipo)
        if resultado_guardado is not None:
            return resultado_guardado

        df_completo = self.datos.cargar_datos()
        df_filtrado = self.datos.filtrar_por_mes(mes)

        if df_filtrado.empty:
            raise ValueError("No se encontraron registros para el mes ingresado.")

        if tipo == "palabra":
            df_filtrado = df_filtrado[df_filtrado["Calculo por"].str.lower() == "palabra"]
            estrategia = CalculoPorPalabra()
        elif tipo == "hora":
            df_filtrado = df_filtrado[df_filtrado["Calculo por"] == "Tiempo"]
            estrategia = CalculoPorHora()
        else:
            raise ValueError("Tipo de cálculo no válido.")

        trabajador = Trabajador(nombre_trabajador, estrategia)
        salario = trabajador.calcular_salario_mensual(df_filtrado)

        # Guardar resultado calculado
        guardar_resultado_salario(nombre_trabajador, mes, tipo, salario)

        return salario
