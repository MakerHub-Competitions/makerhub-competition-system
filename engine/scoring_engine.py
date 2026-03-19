class ScoringEngine:

    def __init__(self):
        self.weights = {
            "accuracy": 0.4,
            "speed": 0.3,
            "quality": 0.2,
            "safety": 0.1
        }

    def score_accuracy(self, deviation_mm):
        if deviation_mm <= 0.05:
            return 100
        elif deviation_mm >= 0.20:
            return 0
        else:
            return int(100 * (1 - (deviation_mm - 0.05) / (0.20 - 0.05)))

    def score_speed(self, minutes):
        target = 60
        if minutes <= target:
            return 100
        else:
            penalty = (minutes - target) / target
            return max(0, int(100 * (1 - penalty)))

    def score_quality(self, defects):
        return max(0, 100 - (defects * 10))

    def score_safety(self, violations):
        return 0 if violations > 0 else 100

    def total_score(self, results):
        total = 0

        total += self.score_accuracy(results["deviation"]) * self.weights["accuracy"]
        total += self.score_speed(results["time"]) * self.weights["speed"]
        total += self.score_quality(results["defects"]) * self.weights["quality"]
        total += self.score_safety(results["violations"]) * self.weights["safety"]

        return int(total)
