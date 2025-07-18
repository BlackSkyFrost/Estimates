from firebase_admin import firestore, initialize_app, credentials

def base_init(route):
    cred = credentials.Certificate(route)
    app = initialize_app(cred)
    db = firestore.client()
    return db

def products_base(db):
    docs= db.collection("products").get()
    return docs