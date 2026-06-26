# engines/digital_twin_engine.py

from typing import Dict


class DigitalTwinEngine:
    """
    Simulates two future career paths:
    1. Current path (no improvement)
    2. Optimized path (following recommendations)
    """

    def __init__(
        self,
        current_probability: float,
        monthly_growth_current: float,
        monthly_growth_optimized: float,
        months: int
    ):
        self.current_probability = current_probability
        self.monthly_growth_current = monthly_growth_current
        self.monthly_growth_optimized = monthly_growth_optimized
        self.months = months

    def simulate_current_path(self) -> float:
        """
        Simulate future if user keeps same habits.
        """

        result = (
            self.current_probability +
            (self.monthly_growth_current * self.months)
        )

        return min(round(result, 2), 100)

    def simulate_optimized_path(self) -> float:
        """
        Simulate future if user follows AI advice.
        """

        result = (
            self.current_probability +
            (self.monthly_growth_optimized * self.months)
        )

        return min(round(result, 2), 100)

    def compare_paths(self) -> Dict:
        """
        Compare both career futures.
        """

        current_path = self.simulate_current_path()
        optimized_path = self.simulate_optimized_path()

        difference = optimized_path - current_path

        if difference >= 30:
            impact = "Massive Growth Potential"

        elif difference >= 15:
            impact = "Strong Improvement Possible"

        else:
            impact = "Moderate Improvement"

        return {
            "current_path_probability": current_path,
            "optimized_path_probability": optimized_path,
            "career_difference": difference,
            "impact_level": impact
        }


# Example test run
if __name__ == "__main__":

    twin = DigitalTwinEngine(
        current_probability=55,
        monthly_growth_current=1.5,
        monthly_growth_optimized=6,
        months=6
    )

    report = twin.compare_paths()

    print(report)