# core/orchestrator.py

from engines.behavior_engine import BehaviorEngine
from engines.skill_gap_engine import SkillGapEngine
from engines.placement_predictor import PlacementPredictor
from engines.future_simulator import FutureSimulator
from engines.digital_twin_engine import DigitalTwinEngine
from engines.adaptive_learning_engine import AdaptiveLearningEngine
from agents.mentor_agent import MentorAgent


class CortexOrchestrator:
    """
    Main AI Brain that controls all Cortex AI modules.
    """

    def run_pipeline(self):

        # -----------------------------
        # STEP 1 : Behavior Analysis
        # -----------------------------
        behavior = BehaviorEngine(
            coding_hours=[2, 4, 3, 0, 5, 6, 2],
            github_commits=18,
            leetcode_solved=22
        )

        behavior_report = behavior.generate_behavior_report()

        # -----------------------------
        # STEP 2 : Skill Gap Analysis
        # -----------------------------
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

        skill_engine = SkillGapEngine(
            current_skills=current_skills,
            required_skills=required_skills
        )

        skill_report = skill_engine.generate_skill_report()

        # -----------------------------
        # STEP 3 : Placement Prediction
        # -----------------------------
        predictor = PlacementPredictor(
            resume_score=80,
            dsa_score=60,
            project_score=90,
            communication_score=70,
            consistency_score=int(
                behavior_report["consistency_score"]
            )
        )

        placement_report = predictor.generate_prediction_report()

        # -----------------------------
        # STEP 4 : Future Simulation
        # -----------------------------
        simulator = FutureSimulator(
            current_probability=placement_report[
                "placement_probability"
            ],
            monthly_improvement_rate=4.5,
            months=6
        )

        future_report = simulator.generate_future_report()

        # -----------------------------
        # STEP 5 : Mentor Agent
        # -----------------------------
        mentor = MentorAgent(
            consistency_score=behavior_report[
                "consistency_score"
            ],
            missing_skills=skill_report[
                "missing_skills"
            ],
            placement_probability=placement_report[
                "placement_probability"
            ],
            future_probability=future_report[
                "future_probability"
            ]
        )

        mentor_report = mentor.generate_recommendation()

        # -----------------------------
        # STEP 6 : Digital Twin
        # -----------------------------
        twin = DigitalTwinEngine(
            current_probability=placement_report[
                "placement_probability"
            ],
            monthly_growth_current=1.5,
            monthly_growth_optimized=6,
            months=6
        )

        twin_report = twin.compare_paths()

        # -----------------------------
        # STEP 7 : Adaptive Learning
        # -----------------------------
        adaptive = AdaptiveLearningEngine(
            previous_strategy="Solve 3 DSA problems daily",
            user_response="ignored"
        )

        adaptive_report = (
            adaptive.generate_adaptive_report()
        )

        # -----------------------------
        # FINAL REPORT
        # -----------------------------
        final_report = {
            "behavior_analysis": behavior_report,
            "skill_gap_analysis": skill_report,
            "placement_prediction": placement_report,
            "future_simulation": future_report,
            "mentor_analysis": mentor_report,
            "digital_twin_analysis": twin_report,
            "adaptive_learning": adaptive_report
        }

        return final_report


# Test run
if __name__ == "__main__":

    cortex = CortexOrchestrator()

    report = cortex.run_pipeline()

    print(report)