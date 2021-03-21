from datetime import date, timedelta
from .api import edinet
from .api import s3

def get_documents_list():
    target_date = date(2020, 4, 1)
    # target_date = date.today() - timedelta(days=1)
    count = edinet.get_count(target_date=target_date)
    if count == 0:
        return []

    documents = edinet.get_documents(target_date=target_date)
    # @todo filter by availability
    # @todo lambda function response
    # return documents
    return documents[:3]

def get_document(document_id):
    filepath = edinet.get_document(document_id=document_id)

    s3_client = s3.client()
    key = document_id + '.zip'
    s3_client.put_object(key, filepath)
