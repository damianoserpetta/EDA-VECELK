from haystack.nodes.connector import Crawler
import json
import os

from model.static.utils import convert_json_to_dicts


class crawler():
    output_path = ""

    def __init__(self):
        self.output_path = "crawled_files"

    def crawl_from_website(self, _url, _filter_urls):
        crawler = Crawler(self.output_path)

        docs = crawler.crawl(urls=[_url],
                             crawler_depth=1,
                             filter_urls=_filter_urls,
                             overwrite_existing_files=True)
        return docs

    def set_output_dir(self, _path):
        self.output_path = _path
