class IdentitySeed:
    """Shapes behavior style through traits."""

    def __init__(self):
        self.identity = {
            "safety": 0.8,
            "efficiency": 0.7,
            "curiosity": 0.5,
            "boldness": 0.4,
            "clarity": 0.8,
        }

    def choose(self, actions, context="normal"):
        best_action = None
        best_score = float("-inf")

        for action_name, profile in actions.items():
            score = sum(self.identity.get(trait, 0) * value for trait, value in profile.items())

            if score > best_score:
                best_score = score
                best_action = action_name

        return best_action
