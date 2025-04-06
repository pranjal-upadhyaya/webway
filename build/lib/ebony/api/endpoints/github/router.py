from fastapi import APIRouter, Depends, status
from ebony.domain.github.service_handlers.githib_service import GithubService
from ebony.utilities.api_response import APIResponse
from ebony.api.module import get_injector_instance

router = APIRouter(prefix="/github", tags=["github"])

def get_github_service() -> GithubService:
    return get_injector_instance(GithubService)

@router.get("/repos")
def get_repos(
    github_service: GithubService = Depends(get_github_service)
):
    """Get user's GitHub repositories."""

    response = github_service.get_repositories()
    return APIResponse(
        data=response,
        message="Repositories fetched successfully",
        status_code=status.HTTP_200_OK
    )

@router.get("/repos/{repo_name}")
def get_repo(
    repo_name: str,
    github_service: GithubService = Depends(get_github_service)
):
    """Get a specific GitHub repository."""
    response = github_service.get_repository(repo_name)
    return APIResponse(
        data=response,
        message="Repository fetched successfully",
        status_code=status.HTTP_200_OK
    )

@router.get("/repos/{repo_name}/activity")
def get_repo_activity(
    repo_name: str,
    github_service: GithubService = Depends(get_github_service)
):
    """Get activity of a specific GitHub repository."""
    response = github_service.get_repository_activity(repo_name)
    return APIResponse(
        data=response,
        message="Repository activity fetched successfully",
        status_code=status.HTTP_200_OK
    )
