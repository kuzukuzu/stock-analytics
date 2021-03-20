import boto3

class Client:
  def __init__(self, bucket):
    self.__client = boto3.client('s3')
    self.__bucket = bucket

  def put_object(self, key, filepath):
    self.__client.put_object(
      Bucket=self.__bucket,
      Key=key,
      Body=filepath
    )

class DummyClient(Client):
  def put_object(self, key, filepath):
    pass

def client():
  return Client('lake-edinet-dev')
