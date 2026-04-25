class ToolSeed:
    """Registers, selects, and executes tools with feedback."""

    def __init__(self):
        self.tools = {}

    def register_tool(self, tool):
        self.tools[tool.name] = {
            "tool": tool,
            "risk": tool.risk,
            "usage": 0,
            "success": 0,
            "failure": 0,
        }

    def list_tools(self):
        return list(self.tools.keys())

    def execute(self, tool_name, input_data, safety_layer):
        if tool_name not in self.tools:
            return {"ok": False, "error": f"Tool not found: {tool_name}"}

        record = self.tools[tool_name]
        tool = record["tool"]

        if not safety_layer.allow(tool.risk):
            return {"ok": False, "error": f"Blocked by safety layer: {tool.risk}"}

        result = tool.run(input_data)

        record["usage"] += 1
        if result.get("ok"):
            record["success"] += 1
        else:
            record["failure"] += 1

        return result
