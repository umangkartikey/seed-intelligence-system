from collections import Counter


class ReflectionSeed:
    """Analyzes results and detects repeated reasoning/tool issues."""

    def __init__(self):
        self.reflections = []
        self.patterns = Counter()
        self.reasoning_rules = []

    def analyze(self, task, plan, results, success, reward):
        issues = []

        if not success:
            issues.append("task_failed")

        if reward < 0:
            issues.append("low_reward")

        for step_result in results:
            step = step_result.get("step", {})
            result = step_result.get("result", {})
            tool = step.get("tool", "unknown")

            if result.get("ok") is False:
                issues.append(f"tool_failed:{tool}")

        for issue in issues:
            self.patterns[issue] += 1

        reflection = {
            "task": task,
            "success": success,
            "reward": reward,
            "issues": issues,
            "suggestions": self.suggest(),
        }

        self.reflections.append(reflection)
        return reflection

    def suggest(self):
        suggestions = []

        if self.patterns["low_reward"] >= 3:
            suggestions.append("revise_reward_strategy")

        if self.patterns["task_failed"] >= 3:
            suggestions.append("split_tasks_into_smaller_steps")

        for issue, count in self.patterns.items():
            if issue.startswith("tool_failed") and count >= 2:
                tool = issue.split(":", 1)[1]
                suggestions.append(f"repair_or_replace_tool:{tool}")

        return suggestions
