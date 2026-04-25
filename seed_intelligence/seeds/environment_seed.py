import random


class EnvironmentSeed:
    """Generates adaptive scenarios for testing."""

    def __init__(self):
        self.level = 1
        self.scenarios = [
            "research_task",
            "calculation_task",
            "tool_failure_test",
            "memory_noise_test",
        ]

    def generate_scenario(self):
        scenario = random.choice(self.scenarios)
        return {
            "scenario": scenario,
            "level": self.level,
            "risk": 0.2 * self.level,
        }

    def adjust_difficulty(self, performance_score):
        if performance_score > 5:
            self.level += 1
        elif performance_score < -5:
            self.level = max(1, self.level - 1)
