from fastapi import APIRouter, HTTPException, status
import requests
from ebony.constants.config import app_config

router = APIRouter(prefix="/github", tags=["github"])

@router.get("/repos")
async def get_repos():
    """Get user's GitHub repositories."""
    response = requests.get(
        f"https://api.github.com/users/{app_config.github_owner}/repos",
        headers={
            "Authorization": f"Bearer {app_config.github_access_token}",
            "Accept": "application/vnd.github.v3+json",
        }
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {app_config.github_owner} not found"
        )
    return response.json()

@router.get("/repos/{repo_name}")
async def get_repo(repo_name: str):
    """Get a specific GitHub repository."""
    response = requests.get(
        f"https://api.github.com/repos/{app_config.github_owner}/{repo_name}",
        headers={
            "Authorization": f"Bearer {app_config.github_access_token}",
            "Accept": "application/vnd.github.v3+json",
        }
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Repository {repo_name} not found"
        )
    return response.json()

@router.get("/repos/{repo_name}/activity")
def get_repo_activity(repo_name: str):
    """Get activity of a specific GitHub repository."""
    response = requests.get(
        f"https://api.github.com/repos/{app_config.github_owner}/{repo_name}/activity",
        headers={
            "Authorization": f"Bearer {app_config.github_access_token}",
            "Accept": "application/vnd.github.v3+json",
        }
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Repository {repo_name} not found"
        )
    return response.json()