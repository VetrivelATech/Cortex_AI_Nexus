from pydantic import BaseModel

class GitHubRequest(BaseModel):
    repo_count: int
    commit_count: int
    languages_used: int
    readme_quality: int
    open_source_contributions: int