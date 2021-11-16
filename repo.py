from elasticsearch import Elasticsearch
from config.elastic import ElasticConfig
from elasticsearch.connection import create_ssl_context
import ssl

ssl_context = create_ssl_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

class Elastic:
    def __init__(self):
        self.config = ElasticConfig()
        self.client = self.set_client()

    def set_client(self):
        # return Elasticsearch(headers={"accept": "application/vnd.elasticsearch+json; compatible-with=7"}, host=self.config.HOST, port=self.config.PORT, http_auth=(self.config.USER, self.config.PASS), verify_certs=False, use_ssl=bool(self.config.SSL), ca_certs=certifi.where())
        return Elasticsearch(hosts=[{'host': self.config.HOST, 'port': self.config.PORT}],
                       scheme="http",
                       verify_certs=False,
                       ssl_context=ssl_context,
                       http_auth=(self.config.USER, self.config.PASS))


    def insert(self, data, indexname):
        self.client.index(index=indexname, doc_type='map', body=data)