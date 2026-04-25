# Architecture

## Seed Mind Loop

```text
1. Receive task / environment state
2. GoalSeed decides direction
3. Planner creates a step sequence
4. IdentitySeed shapes behavior
5. ToolSeed executes tools safely
6. MemorySeed stores experience
7. ReflectionSeed analyzes result
8. MetaSeed may propose improvements
9. SafetyLayer approves/rejects changes
```

## Data Flow

```text
Task
 ↓
GoalSeed ──→ Planner ──→ ToolSeed ──→ Result
 ↓                         ↓
IdentitySeed              SafetyLayer
 ↓                         ↓
MemorySeed ←──────── ReflectionSeed
 ↓
MetaSeed / NetworkSeed
```

## Design Rule

Each seed should be independently testable.

```text
seed = small module
engine = orchestration layer
safety = non-negotiable boundary
```
