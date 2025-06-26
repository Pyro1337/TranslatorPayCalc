class Productividad:
    def __init__(self, cantidad: float, precio_unitario: float, cotizacion: float):
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.cotizacion = cotizacion

    def obtener_total_guaranies(self) -> float:
        return self.cantidad * self.precio_unitario * self.cotizacion


class Trabajador:
    def __init__(self, nombre: str, estrategia):
        self.nombre = nombre
        self.estrategia = estrategia

    def calcular_salario_mensual(self, df_filtrado) -> float:
        return self.estrategia.calcular_salario_final(df_filtrado)
