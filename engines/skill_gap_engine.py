class SkillGapEngine:

    def __init__(self):
        # predefined role skills
        self.role_skills = {
            "ai engineer": [
                "python", "machine learning", "deep learning",
                "tensorFlow", "sql", "docker", "aws"
            ],

            "data scientist": [
                "python", "pandas", "numpy",
                "machine learning", "sql", "tableau"
            ],

            "ml engineer": [
                "python", "machine learning",
                "tensorFlow", "docker", "aws", "git"
            ]
        }

    def analyze_skill_gap(self, target_role, user_skills):

        target_role = target_role.lower()

        required_skills = self.role_skills.get(target_role, [])

        missing_skills = []

        for skill in required_skills:
            if skill.lower() not in [s.lower() for s in user_skills]:
                missing_skills.append(skill)

        readiness_score = int(
            ((len(required_skills) - len(missing_skills))
             / len(required_skills)) * 100
        )

        return {
            "target_role": target_role,
            "missing_skills": missing_skills,
            "readiness_score": readiness_score
        }