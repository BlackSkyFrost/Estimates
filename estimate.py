import fbase
route = r'C:\Users\gesta\Downloads\ahoy-2326b-d66bd72aa380.json'
base = fbase.base_init(route)
products = fbase.products_base(base)
# Comenzar desde una colección raíz
for doc in base.collection('products').stream():
    fbase.recorrer_documento(doc)
base.close()