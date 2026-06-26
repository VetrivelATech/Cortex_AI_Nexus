# engines/adaptive_learning_engine.py

from typing import Dict


class AdaptiveLearningEngine:
    """
    Adaptive Learning Engine modifies recommendation strategy
    based on user response to previous advice.
    """

    def __init__(
        self,
        previous_strategy: str,
        user_response: str
    ):
        self.previous_strategy = previous_strategy
        self.user_response = user_response.lower()

    def adapt_strategy(self) -> str:
        """
        Change strategy based on user response.
        """

        if self.user_response == "ignored":
            if "3 DSA" in self.previous_strategy:
                return "Start with 1 easy DSA problem daily."

            elif "backend project" in self.previous_strategy:
                return "Build a small API project first."

            else:
                return "Reduce workload and start smaller tasks."

        elif self.user_response == "completed":
            return "Increase challenge level gradually."

        elif self.user_response == "partial":
            return "Maintain current strategy with lighter schedule."

        else:
            return "Observe more user behavior before changing strategy."

    def calculate_adaptation_score(self) -> int:
        """
        Estimate adaptation effectiveness score.
        """

        if self.user_response == "completed":
            return 95

        elif self.user_response == "partial":
            return 75

        elif self.user_response == "ignored":
            return 85

        return 50

    def generate_adaptive_report(self) -> Dict:
        """
        Final adaptive learning report.
        """

        return {
            "previous_strategy": self.previous_strategy,
            "user_response": self.user_response,
            "new_strategy": self.adapt_strategy(),
            "adaptation_score": self.calculate_adaptation_score()
        }


# Example test run
if __name__ == "__main__":

    engine = AdaptiveLearningEngine(
        previous_strategy="Solve 3 DSA problems daily",
        user_response="ignored"
    )

    report = engine.generate_adaptive_report()

    print(report)