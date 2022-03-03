from fastapi import APIRouter
from schema import ScrapeRequest
import model.application as application
router = APIRouter()


@router.post("/scrape")
def crawl(request: ScrapeRequest):
    ack = application.search_engine_app.scrape_ingest_web_page(
        request.url, request.filter)
    return ack
