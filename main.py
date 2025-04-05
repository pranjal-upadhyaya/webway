from ebony.constants.config import app_config
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "ebony.app:app",
        host=app_config.app_host,
        port=app_config.app_port,
        reload=True,
    )
