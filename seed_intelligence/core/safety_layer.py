class SafetyLayer:
    """Basic safety gate for tool execution."""

    def __init__(self):
        self.allowed_risk = {
            "low": True,
            "medium": True,
            "high": False,
        }

    def allow(self, risk: str) -> bool:
        return self.allowed_risk.get(risk, False)
