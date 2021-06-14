FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["mongo_client.py"]
ENTRYPOINT ["python3"]
RUN pip install pymongo
