import os

class ElasticConfig:
    HOST = os.environ.get('ES_HOST')
    USER = os.environ.get('ES_USER')
    PASS = os.environ.get('ES_PASS')
    PORT = os.environ.get('ES_PORT')
    SSL = os.environ.get('ES_SSL')