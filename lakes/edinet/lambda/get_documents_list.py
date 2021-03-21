from . import main

def handler(event, context):
    return main.get_documents_list()
