class FutureSimulator:

    def simulate(self, study_hours, projects, consistency):

        score = 40

        score += study_hours * 5
        score += projects * 8
        score += consistency * 0.3

        if score > 100:
            score = 100

        if score >= 85:
            status = "Excellent Future"
        elif score >= 70:
            status = "Good Growth"
        else:
            status = "Need Improvement"

        return {
            "future_score": score,
            "status": status,
            "google_chance": min(score - 5, 100),
            "startup_chance": min(score + 5, 100),
            "advice": [
                "Build more projects",
                "Practice DSA daily",
                "Stay consistent"
            ]
        }