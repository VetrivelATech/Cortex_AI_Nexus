# engines/future_simulator.py

from typing import Dict


class FutureSimulator:
    """
    Simulates future placement probability
    based on current progress and improvement rate.
    """

    def __init__(
        self,
        current_probability: float,
        monthly_improvement_rate: float,
        months: int
    ):
        self.current_probability = current_probability
        self.monthly_improvement_rate = monthly_improvement_rate
        self.months = months

    def calculate_future_probability(self) -> float:
        """
        Predict future probability after n months.
        """

        future_probability = (
            self.current_probability +
            (self.monthly_improvement_rate * self.months)
        )

        # cap maximum probability at 100
        if future_probability > 100:
            future_probability = 100

        return round(future_probability, 2)

    def classify_future_status(self, probability: float) -> str:
        """
        Classify future career growth status.
        """

        if probability >= 90:
            return "Excellent Career Growth"

        elif probability >= 75:
            return "Strong Career Growth"

        elif probability >= 55:
            return "Average Growth"

        else:
            return "Needs Major Improvement"

    def generate_future_report(self) -> Dict:
        """
        Final future simulation report.
        """

        future_probability = self.calculate_future_probability()

        return {
            "current_probability": self.current_probability,
            "future_probability": future_probability,
            "months_simulated": self.months,
            "future_status": self.classify_future_status(
                future_probability
            )
        }


# Example test run
if __name__ == "__main__":

    simulator = FutureSimulator(
        current_probability=72,
        monthly_improvement_rate=4.5,
        months=6
    )

    report = simulator.generate_future_report()
    print(report)