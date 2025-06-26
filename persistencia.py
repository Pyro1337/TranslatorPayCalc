import pickle
import os

def obtener_nombre_archivo(nombre: str, mes: str, tipo: str) -> str:
    """Genera un nombre de archivo único para guardar resultados de salario"""
    base_dir = "salarios_guardados"
    os.makedirs(base_dir, exist_ok=True)
    return os.path.join(base_dir, f"{nombre}_{mes}_{tipo}.pkl")

def guardar_resultado_salario(nombre: str, mes: str, tipo: str, salario: float):
    """Guarda el resultado del cálculo de salario en un archivo .pkl con estructura completa"""
    ruta = obtener_nombre_archivo(nombre, mes, tipo)
    with open(ruta, "wb") as f:
        datos = {
            "nombre": nombre,
            "mes": mes,
            "tipo": tipo,
            "salario": salario
        }
        pickle.dump(datos, f)

def cargar_resultado_salario(nombre: str, mes: str, tipo: str):
    """Carga un resultado de salario guardado antes si es que ya existe"""
    ruta = obtener_nombre_archivo(nombre, mes, tipo)
    if os.path.exists(ruta):
        with open(ruta, "rb") as f:
            return pickle.load(f)
    return None
