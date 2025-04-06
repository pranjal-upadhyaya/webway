from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any
from datetime import datetime


class GithubRepository(BaseModel):
    id: int
    name: str
    full_name: str
    description: Optional[str] = None
    private: bool
    html_url: str
    url: str
    owner: dict  # Could be expanded into a separate Owner model
    fork: bool
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    size: int
    stargazers_count: int
    watchers_count: int
    language: Optional[str] = None
    has_issues: bool
    has_projects: bool
    has_wiki: bool
    open_issues_count: int
    forks_count: int
    default_branch: str
    visibility: str

class GithubActor(BaseModel):
    login: str
    id: int
    node_id: Optional[str] = None
    avatar_url: str
    gravatar_id: Optional[str] = ""
    url: str
    html_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    organizations_url: Optional[str] = None
    repos_url: Optional[str] = None
    events_url: Optional[str] = None
    received_events_url: Optional[str] = None
    type: Optional[str] = None
    user_view_type: Optional[str] = None
    site_admin: Optional[bool] = False

class GithubRepositoryActivity(BaseModel):
    id: int
    node_id: Optional[str] = None
    before: Optional[str] = None  # Commit hash before the activity
    after: Optional[str] = None   # Commit hash after the activity
    ref: Optional[str] = None     # Branch reference (e.g., "refs/heads/main")
    timestamp: Optional[datetime] = None
    created_at: Optional[str] = None  # Alternative timestamp format
    activity_type: Optional[str] = Field(None, alias="type")  # Allowing for 'type' field in JSON
    actor: GithubActor
    
    class Config:
        populate_by_name = True  # Allow population by alias

class GetGithubRepositoryResponse(GithubRepository):
    pass

class GetGithubRepositoriesResponse(BaseModel):
    repos: list[GithubRepository]

class GetGithubRepositoryActivityResponse(BaseModel):
    activities: list[GithubRepositoryActivity]

    
    

