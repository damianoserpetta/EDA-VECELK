from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from controller.router import router as api_router


def get_application() -> FastAPI:

    app = FastAPI(title="DA Project", version="1.0.0")
    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
    )
    #app.add_exception_handler(HTTPException, http_error_handler)
    app.include_router(api_router)

    return app
