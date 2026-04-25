from seed_intelligence.core.seed_engine import SeedEngine
from seed_intelligence.core.planner import AdaptivePlanner
from seed_intelligence.core.safety_layer import SafetyLayer

from seed_intelligence.seeds.memory_seed import MemorySeed
from seed_intelligence.seeds.goal_seed import GoalSeed
from seed_intelligence.seeds.identity_seed import IdentitySeed
from seed_intelligence.seeds.reflection_seed import ReflectionSeed
from seed_intelligence.seeds.tool_seed import ToolSeed

from seed_intelligence.tools.calculator_tool import CalculatorTool
from seed_intelligence.tools.note_writer_tool import NoteWriterTool


def build_engine():
    tool_seed = ToolSeed()
    tool_seed.register_tool(CalculatorTool())
    tool_seed.register_tool(NoteWriterTool())

    return SeedEngine(
        tool_seed=tool_seed,
        memory_seed=MemorySeed(),
        goal_seed=GoalSeed(),
        identity_seed=IdentitySeed(),
        reflection_seed=ReflectionSeed(),
        safety_layer=SafetyLayer(),
        planner=AdaptivePlanner(),
    )


if __name__ == "__main__":
    engine = build_engine()

    tasks = [
        "calculate 12 * (5 + 3)",
        "remember Seed Intelligence System started from a cute code seed.",
        "calculate 10 / 2 + 7",
    ]

    for task in tasks:
        output = engine.run_task(task)
        print("\nTask:", output["task"])
        print("Goal:", output["goal"])
        print("Plan:", output["plan"])
        print("Success:", output["success"])
        print("Reward:", output["reward"])
        print("Results:", output["results"])
        print("Reflection:", output["reflection"])
