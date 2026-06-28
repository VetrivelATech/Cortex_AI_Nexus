from engines.behavior_engine import BehaviorEngine
from engines.skill_gap_engine import SkillGapEngine
from engines.placement_predictor import PlacementPredictor
from engines.future_simulator import FutureSimulator


class CortexOrchestrator:

    def run_pipeline(self):

        # ----------------------------
        # STEP 1 : Behavior Analysis
        # ----------------------------
        behavior = BehaviorEngine(
            coding_hours=[2, 4, 3, 5, 6, 2],
            github_commits=15,
            leetcode_solved=22
        )

        behavior_report = behavior.generate_behavior_report()

        # ----------------------------
        # STEP 2 : Skill Gap Analysis
        # ----------------------------
        skill_engine = SkillGapEngine()

        skill_report = skill_engine.analyze_skill_gap(
            target_role="ai engineer",
            user_skills=["python", "sql", "git"]
        )

        # ----------------------------
        # STEP 3 : Placement Prediction
        # ----------------------------
        predictor = PlacementPredictor(
            resume_score=80,
            dsa_score=60,
            project_score=90,
            communication_score=70,
            consistency_score=80
        )

        placement_report = predictor.generate_prediction_report()

        # ----------------------------
        # STEP 4 : Future Simulation
        # ----------------------------
        simulator = FutureSimulator()

        future_report = simulator.simulate(
            study_hours=3,
            projects=2,
            consistency=80
        )

        # ----------------------------
        # FINAL REPORT
        # ----------------------------
        final_report = {
            "behavior_analysis": behavior_report,
            "skill_gap_analysis": skill_report,
            "placement_prediction": placement_report,
            "future_simulation": future_report
        }

        return final_report


# test
if __name__ == "__main__":
    cortex = CortexOrchestrator()
    report = cortex.run_pipeline()
    print(report)