from canbench.scenarios import nominal, stress, dropouts, fuzz_invalid

def test_imports():
    assert nominal is not None
    assert stress is not None
    assert dropouts is not None
    assert fuzz_invalid is not None
