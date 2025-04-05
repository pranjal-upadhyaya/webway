from ebony.constants.config import app_config
import uvicorn

from fastapi import FastAPI

app = FastAPI(
    title="Webway API",
    description="API for Webway application",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Welcome to Webway API"} 

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_config.app_host,
        port=app_config.app_port,
        reload=True,
    )
