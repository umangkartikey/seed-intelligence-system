from seed_intelligence.examples.demo import build_engine


def test_calculator_task():
    engine = build_engine()
    result = engine.run_task("calculate 2 + 2")
    assert result["success"] is True
    assert result["results"][0]["result"]["result"] == 4
