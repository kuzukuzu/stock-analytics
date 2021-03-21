from . import main

def handler(event, context):
    return main.get_document(document_id=event['docID'])
