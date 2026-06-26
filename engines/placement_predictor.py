class PlacementPredictor:

    def __init__(self, resume_score, dsa_score, project_score, communication_score, consistency_score):
        self.resume_score = resume_score
        self.dsa_score = dsa_score
        self.project_score = project_score
        self.communication_score = communication_score
        self.consistency_score = consistency_score

    def calculate_probability(self):
        avg = (
            self.resume_score +
            self.dsa_score +
            self.project_score +
            self.communication_score +
            self.consistency_score
        ) / 5
        return round(avg, 2)

    def get_status(self, probability):
        if probability >= 80:
            return "Very High Chance"
        elif probability >= 60:
            return "High Chance"
        else:
            return "Low Chance"

    def generate_prediction_report(self):

        probability = self.calculate_probability()

        weak_areas = []
        recommendations = []

        if self.dsa_score < 60:
            weak_areas.append("DSA")
            recommendations.append("Practice Leetcode daily")

        if self.project_score < 60:
            weak_areas.append("Projects")
            recommendations.append("Build strong AI projects")

        if self.communication_score < 60:
            weak_areas.append("Communication")
            recommendations.append("Practice mock interviews")

        if self.resume_score < 60:
            weak_areas.append("Resume")
            recommendations.append("Improve ATS resume")

        if self.consistency_score < 60:
            weak_areas.append("Consistency")
            recommendations.append("Maintain daily learning streak")

        return {
            "placement_probability": probability,
            "status": self.get_status(probability),
            "weak_areas": weak_areas,
            "recommendations": recommendations
        }