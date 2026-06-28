# engines/interview_engine.py

class InterviewEngine:

    def __init__(self):
        self.questions_db = {
            "AI Engineer": [
                "Explain supervised vs unsupervised learning",
                "What is overfitting in machine learning?",
                "Difference between CNN and RNN?",
                "Explain gradient descent",
                "How does a decision tree work?"
            ],
            "Data Scientist": [
                "What is feature engineering?",
                "Explain linear regression",
                "Difference between classification and clustering?",
                "What is bias variance tradeoff?",
                "Explain confusion matrix"
            ]
        }

    def generate_questions(self, role):
        questions = self.questions_db.get(
            role,
            ["Tell me about yourself"]
        )

        return {
            "role": role,
            "questions": questions,
            "difficulty": "Medium",
            "mock_score": 75,
            "suggestions": [
                "Practice technical fundamentals",
                "Improve communication",
                "Revise projects thoroughly"
            ]
        }