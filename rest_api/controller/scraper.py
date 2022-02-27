from fastapi import APIRouter
from rest_api.schema import ScrapeRequest
import application
router = APIRouter()


@router.post("/scrape")
def search_query(request: ScrapeRequest):
    ack = application.search_engine.scrape_ingest_web_page(
        request.url, request.filter)
    return ack
