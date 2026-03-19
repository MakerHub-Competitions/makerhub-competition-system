from engine.competition_generator import CompetitionGenerator
from engine.scoring_engine import ScoringEngine
import json

generator = CompetitionGenerator()
scorer = ScoringEngine()

competition = generator.generate_competition()

# Simulated real-world results
results = {
    "deviation": 0.08,
    "time": 72,
    "defects": 1,
    "violations": 0
}

score = scorer.total_score(results)

print("\n=== GENERATED COMPETITION ===\n")
print(json.dumps(competition, indent=4))

print("\n=== PERFORMANCE RESULT ===\n")
print(json.dumps(results, indent=4))

print(f"\n=== FINAL SCORE: {score}/100 ===\n")
