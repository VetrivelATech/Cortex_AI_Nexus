# engines/skill_gap_engine.py

from typing import Dict, List


class SkillGapEngine:
    """
    Skill Gap Engine compares current skills with
    target job/company skill requirements.
    """

    def __init__(
        self,
        current_skills: Dict[str, int],
        required_skills: Dict[str, int]
    ):
        self.current_skills = current_skills
        self.required_skills = required_skills

    def find_missing_skills(self) -> List[str]:
        """
        Detect skills below required level.
        """

        missing_skills = []

        for skill, required_level in self.required_skills.items():
            current_level = self.current_skills.get(skill, 0)

            if current_level < required_level:
                missing_skills.append(skill)

        return missing_skills

    def calculate_readiness_score(self) -> float:
        """
        Calculate percentage readiness for target role.
        """

        total_required = sum(self.required_skills.values())
        total_current = 0

        for skill, required_level in self.required_skills.items():
            current_level = self.current_skills.get(skill, 0)

            # cap current skill at required level
            total_current += min(current_level, required_level)

        readiness_score = (total_current / total_required) * 100
        return round(readiness_score, 2)

    def improvement_priority(self) -> Dict[str, int]:
        """
        Calculate how much improvement needed per skill.
        """

        priority = {}

        for skill, required_level in self.required_skills.items():
            current_level = self.current_skills.get(skill, 0)

            if current_level < required_level:
                priority[skill] = required_level - current_level

        return priority

    def generate_skill_report(self) -> Dict:
        """
        Final skill analysis report.
        """

        return {
            "readiness_score": self.calculate_readiness_score(),
            "missing_skills": self.find_missing_skills(),
            "improvement_priority": self.improvement_priority()
        }


# Example test run
if __name__ == "__main__":

    current_skills = {
        "python": 8,
        "dsa": 4,
        "system_design": 2,
        "backend": 5
    }

    required_skills = {
        "python": 8,
        "dsa": 8,
        "system_design": 7,
        "backend": 7
    }

    engine = SkillGapEngine(
        current_skills=current_skills,
        required_skills=required_skills
    )

    report = engine.generate_skill_report()
    print(report)