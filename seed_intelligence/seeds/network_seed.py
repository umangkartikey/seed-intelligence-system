class NetworkSeed:
    """Shares trusted memories and tools between SeedEngines."""

    def __init__(self):
        self.nodes = {}
        self.reputation = {}

    def register_node(self, name, seed_engine, trust=0.5):
        self.nodes[name] = seed_engine
        self.reputation[name] = trust

    def broadcast_memory(self, source_name, memory_key):
        source = self.nodes[source_name]
        memory = source.memory_seed.memory.get(memory_key)

        if not memory or memory.get("private"):
            return "not_shared"

        if memory.get("trust", 0.0) < 0.6:
            return "rejected_low_trust"

        for name, node in self.nodes.items():
            if name == source_name:
                continue
            node.memory_seed.store(
                key=memory_key,
                value=memory["value"],
                importance=memory.get("importance", 0.5),
                trust=memory.get("trust", 0.5),
                source=f"shared_from_{source_name}",
            )

        return "shared"
