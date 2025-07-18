import tkinter as tk
from tkinter import messagebox

def opcion1():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Ventana de Opción 1")
    nueva_ventana.geometry("300x150")
    tk.Label(nueva_ventana, text="¡Esta es la ventana de la Opción 1!").pack(pady=20)
    tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack(pady=10)

def opcion2():
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Ventana de Opción 2")
    nueva_ventana.geometry("300x150")
    tk.Label(nueva_ventana, text="¡Esta es la ventana de la Opción 2!").pack(pady=20)
    tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack(pady=10)

def salir(ventana):
    ventana.quit()

