class GoalSeed:
    """Chooses the most important goal."""

    def __init__(self):
        self.goals = {
            "complete_task": {
                "priority": 1.0,
                "progress": 0.0,
            }
        }

    def choose_goal(self):
        return max(self.goals, key=lambda g: self.goals[g]["priority"])

    def update_progress(self, goal, reward):
        if goal not in self.goals:
            return

        if reward > 0:
            self.goals[goal]["progress"] += 0.2

        self.goals[goal]["progress"] = min(1.0, self.goals[goal]["progress"])
