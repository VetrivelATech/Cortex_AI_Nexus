import requests

class GitHubAnalyzer:

    def analyze_github(self, username):
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)

        if response.status_code != 200:
            return {"error": "User not found"}

        repos = response.json()

        repo_count = len(repos)

        languages = []
        for repo in repos:
            if repo["language"]:
                languages.append(repo["language"])

        unique_languages = list(set(languages))

        score = min(repo_count * 10, 100)

        suggestions = []

        if repo_count < 5:
            suggestions.append("Build more projects")

        if len(unique_languages) < 3:
            suggestions.append("Learn more technologies")

        return {
            "repo_count": repo_count,
            "languages": unique_languages,
            "github_score": score,
            "suggestions": suggestions
        }