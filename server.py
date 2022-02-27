import json
import uvicorn
import haystack
from rest_api.schema import QueryRequest, QueryResponse, ScrapeRequest

from rest_api.loader import app_loader
import application

search_engine_app = application.search_engine

app = app_loader.get_application()


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0",
                port=5000, log_level="info")
