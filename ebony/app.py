from fastapi import FastAPI

from ebony.api.router import api_router

app = FastAPI(
    title="Ebony API",
    description="API for Ebony application",
    version="0.1.0",
)

# Include API router
app.include_router(api_router)