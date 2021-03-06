from config import FIRESTORE_CERT

import pprint

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def main():
    cred = credentials.Certificate(FIRESTORE_CERT)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    doc_ref = db.collection('top')
    print(doc_ref)

    docs = doc_ref.get()
    print(docs)
    for doc in docs:
        print(doc)
        pprint(doc.to_dict())

main()
