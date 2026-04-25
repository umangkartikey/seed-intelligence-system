class AdaptivePlanner:
    """Creates simple task plans and remembers outcomes."""

    def __init__(self):
        self.plan_memory = {}

    def task_type(self, task):
        task = task.lower()

        if task.startswith("calculate"):
            return "calculation"

        if task.startswith("remember"):
            return "memory"

        return "unknown"

    def create_plan(self, task):
        task_type = self.task_type(task)

        if task_type == "calculation":
            expression = task.replace("calculate", "", 1).strip()
            return [{"tool": "calculator", "input": {"expression": expression}}]

        if task_type == "memory":
            note = task.replace("remember", "", 1).strip()
            return [{"tool": "note_writer", "input": {"note": note}}]

        return [{"tool": "note_writer", "input": {"note": f"Unknown task: {task}"}}]

    def record_plan_result(self, task, plan, success, reward):
        task_type = self.task_type(task)
        self.plan_memory.setdefault(task_type, []).append({
            "plan": plan,
            "success": success,
            "reward": reward,
        })
