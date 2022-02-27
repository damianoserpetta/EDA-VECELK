
from haystack.utils import clean_wiki_text, convert_files_to_dicts, print_answers
from haystack import Answer
from dicts_processor import process_dicts
from rest_api.schema import QueryResponse
import elastic
import search
import scraper
from config import elastic_config
from utils import convert_json_to_dicts
import os
from typing import Optional

#page_crawl_url = "https://www.industrial-iot.it/en/"
#page_crawl_filter = "industrial-iot\.it\/en\/"


class search_engine():

    melastic = None
    msearch = None
    mscraper = None

    def __init__(self):
        self.melastic = elastic.elastic(
            "localhost", "", "", "document")
        self.msearch = search.search(self.melastic.document_store)
        self.mscraper = scraper.scraper()

    def start(self):
        while(True):
            choose = input(
                "--- Select function ---\n1. Scrape url pages\n2. Ask question\n")
            if choose == '1':
                page_crawl_url = input(
                    "Insert URL: \n")
                page_crawl_filter = input(
                    "Insert Filter: \n")
                self.scrape_ingest_web_page(page_crawl_url, page_crawl_filter)
            elif choose == '2':
                _query = input("Query:\n")
                answer = self.query(_query)
                print("--- Answer: ---\n")
                print_answers(answer, details="minimum")

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
