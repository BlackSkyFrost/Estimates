import fbase
route = r'C:\Users\gesta\Downloads\ahoy-2326b-d66bd72aa380.json'
base = fbase.base_init(route)
products = fbase.products_base(base)
for el in products:
    print(f'{el.id}=>{el.to_dict()}')
base.close()