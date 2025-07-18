from firebase_admin import firestore, initialize_app, credentials

def base_init(route):
    cred = credentials.Certificate(route)
    app = initialize_app(cred)
    db = firestore.client()
    return db

def products_base(db):
    docs= db.collection("products").stream()
    return docs

def recorrer_documento(documento, nivel=0):
    indent = "  " * nivel
    print(f"{indent}Documento: {documento.id}")
    print(f"{indent}Datos: {documento.to_dict()}")

    # Obtener las subcolecciones del documento actual
    subcolecciones = documento.reference.collections()
    for subcol in subcolecciones:
        print(f"{indent}Subcolección: {subcol.id}")
        for subdoc in subcol.stream():
            recorrer_documento(subdoc, nivel + 1)

