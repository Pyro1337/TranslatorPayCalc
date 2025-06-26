import os
import tkinter as tk
from tkinter import messagebox
import calendar
import pickle

from controlador import ControladorSalario
from logica import evaluar_bono

RUTA_SALARIOS = "salarios_guardados"

class InterfazGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salario")
        self.controlador = ControladorSalario("PlanillaCalculo.xlsx")

        tk.Label(root, text="Mes (MM):").grid(row=0, column=0)
        self.mes_entry = tk.Entry(root)
        self.mes_entry.grid(row=0, column=1)

        tk.Label(root, text="Trabajador:").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(root, text="Tipo de cálculo:").grid(row=2, column=0)
        self.tipo_var = tk.StringVar(value="palabra")
        tk.Radiobutton(root, text="Por palabra", variable=self.tipo_var, value="palabra").grid(row=2, column=1, sticky="w")
        tk.Radiobutton(root, text="Por hora", variable=self.tipo_var, value="hora").grid(row=3, column=1, sticky="w")

        tk.Button(root, text="Calcular", command=self.calcular_salario).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Listar salarios guardados", command=self.listar_salarios).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Limpiar salarios guardados", command=self.limpiar_salarios).grid(row=6, column=0, columnspan=2, pady=5)

    def calcular_salario(self):
        mes = self.mes_entry.get().zfill(2)
        nombre = self.nombre_entry.get().strip()
        tipo = self.tipo_var.get()

        try:
            salario = self.controlador.ejecutar_calculo(mes=mes, tipo=tipo, nombre_trabajador=nombre)
            salario_str = f"{salario:,.0f}".replace(",", ".")
            nombre_mes = calendar.month_name[int(mes)].capitalize()

            if evaluar_bono(nombre, salario):
                mensaje = (
                    f"Trabajador: {nombre}\n"
                    f"Mes: {nombre_mes}\n"
                    f"Salario estimado: {salario_str} Gs.\n\n🎉 ¡Elegible para bono!"
                )
            else:
                mensaje = (
                    f"Trabajador: {nombre}\n"
                    f"Mes: {nombre_mes}\n"
                    f"Salario estimado: {salario_str} Gs.\n\n❌ No elegible para bono."
                )

            messagebox.showinfo("Resultado", mensaje)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def listar_salarios(self):
        if not os.path.exists(RUTA_SALARIOS):
            messagebox.showinfo("Salarios", "No hay salarios guardados.")
            return

        archivos = [f for f in os.listdir(RUTA_SALARIOS) if f.endswith(".pkl")]
        if not archivos:
            messagebox.showinfo("Salarios", "No hay salarios guardados.")
            return

        resumen = ""
        for archivo in archivos:
            ruta = os.path.join(RUTA_SALARIOS, archivo)
            with open(ruta, "rb") as f:
                data = pickle.load(f)
                if isinstance(data, dict):
                    resumen += f"{data['nombre']} ({data['mes']}): {data['salario']:,.0f} Gs.\n"
                else:
                    resumen += f"{archivo.replace('.pkl','')}: {data:,.0f} Gs. (formato antiguo)\n"

        messagebox.showinfo("Salarios guardados", resumen)


    def limpiar_salarios(self):
        if not os.path.exists(RUTA_SALARIOS):
            messagebox.showinfo("Salarios", "No hay archivos para eliminar.")
            return

        for archivo in os.listdir(RUTA_SALARIOS):
            if archivo.endswith(".pkl"):
                os.remove(os.path.join(RUTA_SALARIOS, archivo))

        messagebox.showinfo("Salarios", "Todos los salarios guardados han sido eliminados.")

def iniciar_gui():
    root = tk.Tk()
    app = InterfazGUI(root)
    root.mainloop()
