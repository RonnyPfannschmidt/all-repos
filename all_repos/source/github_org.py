from typing import Dict
from typing import NamedTuple

from all_repos import github_api


class Settings(NamedTuple):
    api_key: str
    org: str
    collaborator: bool = True
    forks: bool = False  # noqa: E701 fixed in flake8>=3.6
    private: bool = False


def list_repos(settings: Settings) -> Dict[str, str]:
    repos = github_api.get_all(
        # `/users/<org>/repos` works but `/orgs/<username>/repos` does not
        f'https://api.github.com/users/{settings.org}/repos?per_page=100',
        headers={'Authorization': f'token {settings.api_key}'},
    )
    return github_api.filter_repos(
        repos,
        forks=settings.forks,
        private=settings.private,
        collaborator=settings.collaborator,
    )
