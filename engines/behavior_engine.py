# engines/behavior_engine.py

from typing import List, Dict


class BehaviorEngine:
    """
    Behavior Engine analyzes coding behavior patterns
    and predicts consistency, burnout risk, and performance trend.
    """

    def __init__(
        self,
        coding_hours: List[int],
        github_commits: int,
        leetcode_solved: int
    ):
        self.coding_hours = coding_hours
        self.github_commits = github_commits
        self.leetcode_solved = leetcode_solved

    def calculate_consistency_score(self) -> float:
        """
        Calculate consistency score based on coding activity.
        """

        total_days = len(self.coding_hours)
        active_days = sum(1 for hour in self.coding_hours if hour > 0)

        consistency_score = (active_days / total_days) * 100
        return round(consistency_score, 2)

    def calculate_burnout_risk(self) -> float:
        """
        Detect burnout risk if coding hours are too high continuously.
        """

        avg_hours = sum(self.coding_hours) / len(self.coding_hours)

        if avg_hours >= 8:
            burnout_risk = 80
        elif avg_hours >= 5:
            burnout_risk = 45
        else:
            burnout_risk = 15

        return burnout_risk

    def detect_performance_trend(self) -> str:
        """
        Detect whether performance is improving or declining.
        """

        first_half = self.coding_hours[: len(self.coding_hours)//2]
        second_half = self.coding_hours[len(self.coding_hours)//2:]

        avg_first = sum(first_half) / len(first_half)
        avg_second = sum(second_half) / len(second_half)

        if avg_second > avg_first:
            return "improving"
        elif avg_second < avg_first:
            return "declining"
        else:
            return "stable"

    def generate_behavior_report(self) -> Dict:
        """
        Final behavior analysis report.
        """

        return {
            "consistency_score": self.calculate_consistency_score(),
            "burnout_risk": self.calculate_burnout_risk(),
            "performance_trend": self.detect_performance_trend(),
            "github_commits": self.github_commits,
            "leetcode_solved": self.leetcode_solved
        }


# Example test run
if __name__ == "__main__":
    behavior = BehaviorEngine(
        coding_hours=[2, 4, 3, 0, 5, 6, 2],
        github_commits=18,
        leetcode_solved=22
    )

    report = behavior.generate_behavior_report()
    print(report)