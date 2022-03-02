from fastapi import APIRouter

from rest_api.controller import scraper, search, document

router = APIRouter()

router.include_router(scraper.router, tags=["scraper"])
router.include_router(search.router, tags=["search"])
#router.include_router(document.router, tags=["document"])
