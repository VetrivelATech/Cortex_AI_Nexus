# agents/mentor_agent.py

from typing import Dict, List


class MentorAgent:
    """
    AI Mentor Agent analyzes all engine outputs
    and generates personalized career recommendations.
    """

    def __init__(
        self,
        consistency_score: float,
        missing_skills: List[str],
        placement_probability: float,
        future_probability: float
    ):
        self.consistency_score = consistency_score
        self.missing_skills = missing_skills
        self.placement_probability = placement_probability
        self.future_probability = future_probability

    def analyze_consistency(self) -> str:
        """
        Check coding consistency.
        """

        if self.consistency_score < 60:
            return "Your coding consistency is low. Build daily discipline."

        elif self.consistency_score < 80:
            return "Your coding consistency is moderate. Improve regular practice."

        else:
            return "Excellent coding consistency. Keep momentum."

    def analyze_skills(self) -> str:
        """
        Check missing skill areas.
        """

        if not self.missing_skills:
            return "Your skill profile looks strong."

        skill_list = ", ".join(self.missing_skills)

        return f"Priority skills to improve: {skill_list}"

    def placement_feedback(self) -> str:
        """
        Analyze placement readiness.
        """

        if self.placement_probability >= 80:
            return "You have strong placement readiness."

        elif self.placement_probability >= 60:
            return "Placement chances are good, but improvement needed."

        else:
            return "Placement readiness is currently low."

    def future_feedback(self) -> str:
        """
        Analyze future growth potential.
        """

        if self.future_probability >= 90:
            return "Your future growth trajectory looks excellent."

        elif self.future_probability >= 70:
            return "You are improving well. Continue learning."

        else:
            return "Growth trend is weak. Immediate action required."

    def generate_recommendation(self) -> Dict:
        """
        Final AI mentor report.
        """

        recommendations = []

        if "dsa" in self.missing_skills:
            recommendations.append(
                "Solve 3 DSA problems daily."
            )

        if "backend" in self.missing_skills:
            recommendations.append(
                "Build one backend project this month."
            )

        if self.consistency_score < 60:
            recommendations.append(
                "Maintain a fixed coding schedule every day."
            )

        if len(recommendations) == 0:
            recommendations.append(
                "Keep improving consistently."
            )

        return {
            "consistency_feedback": self.analyze_consistency(),
            "skill_feedback": self.analyze_skills(),
            "placement_feedback": self.placement_feedback(),
            "future_feedback": self.future_feedback(),
            "recommendations": recommendations
        }


# Example test run
if __name__ == "__main__":

    agent = MentorAgent(
        consistency_score=58,
        missing_skills=["dsa", "backend"],
        placement_probability=62,
        future_probability=74
    )

    report = agent.generate_recommendation()

    print(report)