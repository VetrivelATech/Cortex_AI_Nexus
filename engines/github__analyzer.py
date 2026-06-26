# engines/github_analyzer.py

class GitHubAnalyzer:

    def __init__(
        self,
        repo_count,
        commit_count,
        languages_used,
        readme_quality,
        open_source_contributions
    ):

        self.repo_count = repo_count
        self.commit_count = commit_count
        self.languages_used = languages_used
        self.readme_quality = readme_quality
        self.open_source_contributions = open_source_contributions


    def calculate_github_score(self):

        score = (
            self.repo_count * 2 +
            self.commit_count * 0.3 +
            self.languages_used * 5 +
            self.readme_quality * 4 +
            self.open_source_contributions * 6
        )

        return min(score, 100)


    def detect_consistency(self):

        if self.commit_count >= 200:
            return "Excellent"

        elif self.commit_count >= 100:
            return "Good"

        else:
            return "Needs Improvement"


    def recruiter_impression(self):

        score = self.calculate_github_score()

        if score >= 85:
            return "Top Tier Candidate"

        elif score >= 70:
            return "Strong Candidate"

        else:
            return "Average Candidate"


    def generate_github_report(self):

        return {

            "github_score": self.calculate_github_score(),

            "consistency": self.detect_consistency(),

            "recruiter_impression": self.recruiter_impression()
        }



# TEST

if __name__ == "__main__":

    analyzer = GitHubAnalyzer(

        repo_count=12,
        commit_count=180,
        languages_used=5,
        readme_quality=8,
        open_source_contributions=3
    )

    report = analyzer.generate_github_report()

    print(report)