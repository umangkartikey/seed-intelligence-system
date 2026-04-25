class SeedEngine:
    """Main orchestration loop connecting seeds."""

    def __init__(
        self,
        tool_seed,
        memory_seed,
        goal_seed,
        identity_seed,
        reflection_seed,
        safety_layer,
        planner,
    ):
        self.tool_seed = tool_seed
        self.memory_seed = memory_seed
        self.goal_seed = goal_seed
        self.identity_seed = identity_seed
        self.reflection_seed = reflection_seed
        self.safety_layer = safety_layer
        self.planner = planner

    def run_task(self, task):
        goal = self.goal_seed.choose_goal()
        plan = self.planner.create_plan(task)

        results = []
        success = True
        reward = 0

        for step in plan:
            result = self.tool_seed.execute(step["tool"], step["input"], self.safety_layer)
            results.append({"step": step, "result": result})

            if result.get("ok"):
                reward += 1
            else:
                reward -= 1
                success = False
                break

        self.goal_seed.update_progress(goal, reward)
        self.planner.record_plan_result(task, plan, success, reward)

        self.memory_seed.store(
            key=f"task:{task}",
            value={"goal": goal, "plan": plan, "results": results, "success": success, "reward": reward},
            importance=0.8,
            trust=0.8 if success else 0.4,
            source="seed_engine",
        )

        reflection = self.reflection_seed.analyze(task, plan, results, success, reward)

        return {
            "task": task,
            "goal": goal,
            "plan": plan,
            "results": results,
            "success": success,
            "reward": reward,
            "reflection": reflection,
        }
