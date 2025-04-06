from injector import Injector
from ebony.domain.github.modules.github_module import GithubModule

modules = [GithubModule()]

injector = Injector(modules)

def get_injector_instance(service_class: type):
    return injector.get(service_class)
