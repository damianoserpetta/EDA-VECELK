from haystack.nodes import ElasticsearchRetriever
from haystack.nodes import FARMReader, TransformersReader
from haystack.pipelines import ExtractiveQAPipeline


class search():

    pipe = None
    document_store = None

    def __init__(self, _document_store):
        self.document_store = _document_store
        self.pipe = self.build_pipeline()

    def build_pipeline(self):
        retriever = ElasticsearchRetriever(document_store=self.document_store)
        reader = FARMReader(
            model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)
        return ExtractiveQAPipeline(reader, retriever)

    def search_query(self, _query):
        return self.pipe.run(query=_query)
