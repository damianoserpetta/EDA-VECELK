from fastapi import APIRouter

from controller import search, document, crawler

router = APIRouter()

router.include_router(crawler.router, tags=["scraper"])
router.include_router(search.router, tags=["search"])
#router.include_router(document.router, tags=["document"])
