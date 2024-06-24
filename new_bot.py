import tkinter as tk
from tkinter import ttk

class HSVSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Selector de valores HSV")

        # Etiquetas y entradas para valores mínimos de HSV
        ttk.Label(root, text="Hue Mínimo").grid(column=0, row=0, padx=10, pady=5)
        self.hue_min = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.hue_min).grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(root, text="Saturación Mínima").grid(column=0, row=1, padx=10, pady=5)
        self.sat_min = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.sat_min).grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(root, text="Valor Mínimo").grid(column=0, row=2, padx=10, pady=5)
        self.val_min = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.val_min).grid(column=1, row=2, padx=10, pady=5)

        # Etiquetas y entradas para valores máximos de HSV
        ttk.Label(root, text="Hue Máximo").grid(column=0, row=3, padx=10, pady=5)
        self.hue_max = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.hue_max).grid(column=1, row=3, padx=10, pady=5)

        ttk.Label(root, text="Saturación Máxima").grid(column=0, row=4, padx=10, pady=5)
        self.sat_max = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.sat_max).grid(column=1, row=4, padx=10, pady=5)

        ttk.Label(root, text="Valor Máximo").grid(column=0, row=5, padx=10, pady=5)
        self.val_max = tk.DoubleVar()
        ttk.Entry(root, textvariable=self.val_max).grid(column=1, row=5, padx=10, pady=5)

        # Botón para imprimir los valores seleccionados
        self.print_button = ttk.Button(root, text="Imprimir Valores", command=self.print_values)
        self.print_button.grid(column=0, row=6, columnspan=2, pady=10)

    def print_values(self):
        print(f"Hue Mínimo: {self.hue_min.get()}")
        print(f"Saturación Mínima: {self.sat_min.get()}")
        print(f"Valor Mínimo: {self.val_min.get()}")
        print(f"Hue Máximo: {self.hue_max.get()}")
        print(f"Saturación Máxima: {self.sat_max.get()}")
        print(f"Valor Máximo: {self.val_max.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HSVSelector(root)
    root.mainloop()