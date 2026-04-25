import random


class MetaSeed:
    """Generates candidate configs for future evolution."""

    def generate_candidates(self, base_config, count=3):
        candidates = []

        for _ in range(count):
            config = dict(base_config)
            config["exploration"] = random.uniform(0.1, 0.5)
            config["learning"] = random.uniform(0.1, 1.0)
            candidates.append(config)

        return candidates
