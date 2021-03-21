FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY lambda ./lambda
CMD ["lambda.do_nothing.handler"]
