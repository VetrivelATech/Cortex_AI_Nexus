class RoadmapGenerator:

    def generate_roadmap(self, goal, months):

        goal = goal.lower()

        roadmap = {}

        if goal == "ai engineer":

            plan = [
                "Python + DSA Fundamentals",
                "NumPy + Pandas + SQL",
                "Machine Learning Algorithms",
                "Deep Learning + TensorFlow",
                "Docker + AWS + GitHub",
                "Projects + Interview Preparation"
            ]

        elif goal == "data scientist":

            plan = [
                "Python Basics",
                "Pandas + NumPy",
                "Statistics + Probability",
                "Machine Learning",
                "Data Visualization (Power BI/Tableau)",
                "Projects + Resume Building"
            ]

        elif goal == "ml engineer":

            plan = [
                "Python + DSA",
                "Machine Learning Basics",
                "Scikit-learn + Projects",
                "Deep Learning",
                "MLOps + Docker + AWS",
                "Deployment + Interview Prep"
            ]

        else:
            plan = ["Custom roadmap not found"]

        for i in range(min(months, len(plan))):
            roadmap[f"month_{i+1}"] = plan[i]

        return {
            "goal": goal,
            "roadmap": roadmap
        }