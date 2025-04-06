from ebony.domain.github.service_handlers.githib_service import GithubService
from ebony.domain.github.service_handlers.github_service_handler import GithubServiceHandler
from ebony.models.github.github_models import GetGithubRepositoriesResponse, GetGithubRepositoryResponse    
from injector import provider, singleton, Module


class GithubModule(Module):
    
    @provider
    @singleton
    def get_github_service(self) -> GithubService:
        return GithubServiceHandler()
