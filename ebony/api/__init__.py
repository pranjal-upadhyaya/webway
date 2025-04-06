"""API package.""" 


from fastapi import APIRouter

from ebony.api.endpoints.user.router import router as user_router
from ebony.api.endpoints.project.router import router as project_router
from ebony.api.endpoints.github.router import router as github_router

api_router = APIRouter(prefix="/ebony/v0")

# Include all endpoint routers
api_router.include_router(user_router)
api_router.include_router(project_router)
api_router.include_router(github_router)