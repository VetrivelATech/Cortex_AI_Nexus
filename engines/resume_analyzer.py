import fitz   # pymupdf


class ResumeAnalyzer:

    def extract_text(self, file_path):
        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        return text.lower()

    def analyze_resume(self, file_path):
        text = self.extract_text(file_path)

        required_skills = [
            "python",
            "sql",
            "machine learning",
            "deep learning",
            "nlp",
            "tensorflow",
            "react",
            "fastapi",
            "docker",
            "aws",
            "git",
            "data structures",
        ]

        detected = []
        missing = []

        for skill in required_skills:
            if skill in text:
                detected.append(skill)
            else:
                missing.append(skill)

        score = int((len(detected) / len(required_skills)) * 100)

        return {
            "ats_score": score,
            "detected_skills": detected,
            "missing_skills": missing,
            "suggestions": [
                "Improve project descriptions",
                "Add cloud skills",
                "Add deployment experience"
            ]
        }