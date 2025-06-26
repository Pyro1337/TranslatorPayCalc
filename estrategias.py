from abc import ABC, abstractmethod
import pandas as pd
import re
from modelos import Productividad


class EstrategiaCalculoSalario(ABC):
    @abstractmethod
    def calcular_productividad(self, df: pd.DataFrame) -> float:
        pass

    def calcular_salario_final(self, df: pd.DataFrame) -> float:
        total = 0.0
        for _, fila in df.iterrows():
            cantidad = self.calcular_productividad(pd.DataFrame([fila]))
            #En caso de que tengamos inconvenientes en el excel por la , o . hacemos este replace.
            precio = float(str(fila["Precio Unitario"]).replace(",", "."))
            cotizacion = float(str(fila["Cotizacion"]).replace(",", "."))
            productividad = Productividad(cantidad, precio, cotizacion)
            total += productividad.obtener_total_guaranies()
        return total


class CalculoPorPalabra(EstrategiaCalculoSalario):
    def calcular_productividad(self, df: pd.DataFrame) -> float:
        return float(df["CantidadPalabras"].iloc[0])


class CalculoPorHora(EstrategiaCalculoSalario):
    def calcular_productividad(self, df: pd.DataFrame) -> float:
        if df.empty:
            return 0.0

        if "Horas" not in df.columns:
            df["Horas"] = df["TiempoTomado"].apply(self._convertir_a_horas)
        return float(df["Horas"].iloc[0])

    def _convertir_a_horas(self, tiempo_str: str) -> float:
        horas = 0.0
        if not isinstance(tiempo_str, str):
            return 0.0

        h_match = re.search(r"(\d+)h", tiempo_str)
        m_match = re.search(r"(\d+)min", tiempo_str)

        if h_match:
            horas += int(h_match.group(1))
        if m_match:
            horas += int(m_match.group(1)) / 60.0

        return round(horas, 2)

