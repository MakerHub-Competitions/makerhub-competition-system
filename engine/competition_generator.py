import json
import random

class CompetitionGenerator:

    def __init__(self):
        self.competition_types = [
            "Fabrication Challenge",
            "Repair Challenge",
            "Robotics Challenge",
            "Speed Build Challenge"
        ]

        self.materials = [
            "Aluminum",
            "Steel",
            "PLA",
            "Wood",
            "Electronics Kit"
        ]

    def generate_competition(self):
        comp_type = random.choice(self.competition_types)

        competition = {
            "type": comp_type,
            "time_limit_minutes": random.choice([30, 60, 120]),
            "materials": random.sample(self.materials, 3),
            "objective": self.generate_objective(comp_type),
            "scoring": self.generate_scoring(comp_type)
        }

        return competition

    def generate_objective(self, comp_type):
        if comp_type == "Fabrication Challenge":
            return "Build a structurally sound component to specified dimensions."
        elif comp_type == "Repair Challenge":
            return "Diagnose and repair a faulty mechanical or electrical system."
        elif comp_type == "Robotics Challenge":
            return "Program and deploy a robot to complete a defined task."
        else:
            return "Complete the build in the shortest time possible."

    def generate_scoring(self, comp_type):
        return {
            "accuracy": 40,
            "speed": 30,
            "quality": 20,
            "safety": 10
        }