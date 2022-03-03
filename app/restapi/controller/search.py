import haystack
from fastapi import APIRouter
from schema import QueryResponse
import model.application as application
router = APIRouter()


@router.get("/query/{query}", response_model=QueryResponse, response_model_exclude_none=True)
def search_query(_query: str):
    #answer = background_task.add_task(query(_query))
    answer = application.search_engine_app.query(_query)
    return answer


@router.get("/initialized")
def check_status():
    """
    This endpoint can be used during startup to understand if the 
    server is ready to take any requests, or is still loading.

    The recommended approach is to call this endpoint with a short timeout,
    like 500ms, and in case of no reply, consider the server busy.
    """
    return True


@router.get("/hs_version")
def haystack_version():
    """
    Get the running Haystack version.
    """
    return {"hs_version": haystack.__version__}
