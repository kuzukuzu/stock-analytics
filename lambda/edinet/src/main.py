from datetime import date, timedelta
from .api import edinet
from .api import s3

def run():
    target_date = date(2020, 4, 1)
    # target_date = date.today() - timedelta(days=1)
    count = edinet.get_count(target_date=target_date)

    # @todo record count and check
    print(count)

    documents = edinet.get_documents(target_date=target_date)
    if len(documents) == 0:
        return

    # @todo iterate all documents

    document_id = documents[0]['docID']

    filepath = edinet.get_document(document_id=document_id)

    s3_client = s3.client()

    key = target_date.strftime('%Y-%m-%d') + '/' + document_id + '.zip'
    s3_client.put_object(key, filepath)
