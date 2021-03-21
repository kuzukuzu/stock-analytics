from . import main

def handler(event, context):
    main.get_documents_list()
