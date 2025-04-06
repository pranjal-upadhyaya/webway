from abc import abstractmethod
from ebony.models.github.github_models import GetGithubRepositoriesResponse, GetGithubRepositoryResponse


class GithubService:

    @abstractmethod
    def get_repositories(self) -> GetGithubRepositoriesResponse:
        pass

    @abstractmethod
    def get_repository(self, repo_name: str) -> GetGithubRepositoryResponse:
        pass
