from haystack.document_stores import ElasticsearchDocumentStore


class elastic():

    document_store = None

    def __init__(self, _host, _usr, _psw, _index):
        self.document_store = ElasticsearchDocumentStore(
            host=_host, username=_usr, password=_psw, index=_index)

    def write_documents(self, _dicts):
        if(_dicts.__len__ != 0):
            self.document_store.write_documents(_dicts)

    # TODO

    def delete_document(self, _name):
        return True
