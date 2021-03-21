import boto3

class Client:
  def __init__(self, bucket):
    self.__s3 = boto3.resource('s3')
    self.__bucket = self.__s3.Bucket(bucket)

  def upload_file(self, filepath, key):
    self.__bucket.upload_file(
      filepath, key
    )

class DummyClient(Client):
  def upload_file(self, filepath, key):
    pass

def client():
  return Client('lake-edinet-dev')
