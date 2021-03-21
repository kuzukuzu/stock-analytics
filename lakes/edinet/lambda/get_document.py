from . import main

def handler(event, context):
    main.get_document(document_id=event['docID'])
