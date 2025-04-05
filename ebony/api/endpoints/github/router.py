from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/github", tags=["github"])

@router.get("/repos")
async def get_repos():
    """Get user's GitHub repositories."""
    return {"repos": [{"id": 1, "name": "test-repo", "url": "https://github.com/user/test-repo"}]}

@router.get("/repos/{repo_name}")
async def get_repo(repo_name: str):
    """Get a specific GitHub repository."""
    # Mock repo data, in a real app would be from GitHub API
    if repo_name != "test-repo":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Repository {repo_name} not found"
        )
    return {"id": 1, "name": repo_name, "url": f"https://github.com/user/{repo_name}"} 