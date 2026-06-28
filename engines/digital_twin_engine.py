# engines/digital_twin_engine.py

class DigitalTwinEngine:

    def analyze(self, resume_score, github_score, skill_score, consistency):

        avg_score = (resume_score + github_score + skill_score + consistency) / 4

        # personality
        if consistency >= 80:
            personality = "Disciplined Learner"
        elif github_score >= 75:
            personality = "Builder Mindset"
        else:
            personality = "Fast Learner"

        # risk
        if avg_score >= 80:
            career_risk = "Low"
        elif avg_score >= 60:
            career_risk = "Medium"
        else:
            career_risk = "High"

        # strength
        scores = {
            "Resume": resume_score,
            "GitHub": github_score,
            "Skills": skill_score,
            "Consistency": consistency
        }

        top_strength = max(scores, key=scores.get)
        weakness = min(scores, key=scores.get)

        placement_chance = min(avg_score + 10, 100)

        return {
            "personality_type": personality,
            "career_risk": career_risk,
            "top_strength": top_strength,
            "weakness": weakness,
            "placement_chance": placement_chance
        }