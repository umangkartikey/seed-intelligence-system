class CalculatorTool:
    name = "calculator"
    risk = "low"

    def run(self, input_data):
        expression = input_data.get("expression", "")

        allowed = "0123456789+-*/(). "
        if not expression or not all(ch in allowed for ch in expression):
            return {"ok": False, "error": "Unsafe or empty expression"}

        try:
            return {"ok": True, "result": eval(expression, {"__builtins__": {}}, {})}
        except Exception as exc:
            return {"ok": False, "error": str(exc)}
