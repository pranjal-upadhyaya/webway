from fastapi import HTTPException
from ebony.domain.github.service_handlers.githib_service import GithubService
from ebony.models.github.github_models import GetGithubRepositoriesResponse, GetGithubRepositoryActivityResponse, GetGithubRepositoryResponse, GithubRepository, GithubRepositoryActivity
from ebony.constants.config import app_config
import requests

class GithubServiceHandler(GithubService):

    def get_repositories(self) -> GetGithubRepositoriesResponse:

        url = f"https://api.github.com/users/{app_config.github_owner}/repos"
        headers = {
            "Authorization": f"Bearer {app_config.github_access_token}",
            "Accept": "application/vnd.github.v3+json",
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch repositories: {response.status_code}")
        else:
            repositories = [GithubRepository(**repo) for repo in response.json()]

            response = GetGithubRepositoriesResponse(repositories=repositories)
            return response

    def get_repository(self, repo_name: str) -> GetGithubRepositoryResponse:
        url = f"https://api.github.com/repos/{app_config.github_owner}/{repo_name}"
        headers = {
            "Authorization": f"Bearer {app_config.github_access_token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch repository: {response.status_code}")
        else:
            repo = GithubRepository(**response.json())
            return repo
        
    def get_repository_activity(self, repo_name: str) -> GetGithubRepositoryActivityResponse:
        url = f"https://api.github.com/repos/{app_config.github_owner}/{repo_name}/events"
        headers = {
            "Authorization": f"Bearer {app_config.github_access_token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch repository activity: {response.status_code}")
        else:
            activities = [GithubRepositoryActivity(**activity) for activity in response.json()]
            return GetGithubRepositoryActivityResponse(activities=activities)
