import pandas as pd

class GestorDatos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.df = None

    def cargar_datos(self) -> pd.DataFrame:
        try:
            self.df = pd.read_excel(self.nombre_archivo)
            self.df['FechaReclamada'] = pd.to_datetime(self.df['FechaReclamada'], errors='coerce')
            return self.df
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo '{self.nombre_archivo}' en el directorio actual.")

    def filtrar_por_mes(self, mes: str) -> pd.DataFrame:
        if self.df is None:
            raise ValueError("Los datos no fueron cargados aún.")
        return self.df[self.df['FechaReclamada'].dt.strftime('%m') == mes].copy()