
from haystack.utils import clean_wiki_text, convert_files_to_dicts, print_answers
from haystack import Answer
from model.processors.dicts_processor import process_dicts
from rest_api.schema import QueryResponse
import model.datasource.elastic as elastic
import model.search.search as search
import model.crawler.crawler as crawler
from config import elastic_config
from model.static.utils import convert_json_to_dicts
import os
from typing import Optional

class search_engine():

    melastic = None
    msearch = None
    mscraper = None

    def __init__(self):
        self.melastic = elastic.elastic(
            "localhost", "", "", "document")
        self.msearch = search.search(self.melastic.document_store)
        self.mscraper = crawler.crawler()

    def query(self, _question) -> QueryResponse:
        answer = self.msearch.search_query(_question)
        return answer

    def scrape_ingest_web_page(self, url, filterurls):
        docs = self.mscraper.scrape_from_website(url, filterurls)
        dicts = convert_json_to_dicts(docs)

        for filename in docs:
            os.remove(os.path.join(filename.parent, filename.name))
        dicts = process_dicts(dicts)
        self.melastic.write_documents(dicts)
        return True


if __name__ == '__main__':
    app = search_engine()
    app.start()
