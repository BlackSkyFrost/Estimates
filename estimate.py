#import fbase
import methods
# route = r'C:\Users\gesta\Downloads\ahoy-2326b-d66bd72aa380.json'
# base = fbase.base_init(route)
# products = fbase.products_base(base)
# # Comenzar desde una colección raíz
# for doc in base.collection('products').stream():
#     fbase.recorrer_documento(doc)
# base.close()

ventana = methods.tk.Tk()
ventana.title("Cotizador")
ventana.geometry("400x250")
ventana.iconbitmap(r'C:\Users\gesta\Downloads\favicon.ico')
mensaje = methods.tk.Label(ventana, text="Bienvenido seleccione: ", font=("Arial", 12))
mensaje.pack(pady=10)
methods.tk.Button(ventana, text="Crear Proyecto", width=20, command=methods.opcion1).pack(pady=5)
methods.tk.Button(ventana, text="Actualizar Proyecto", width=20, command=methods.opcion2).pack(pady=5)
methods.tk.Button(ventana, text="Salir", width=20, command=lambda:methods.salir(ventana)).pack(pady=5)

ventana.mainloop()