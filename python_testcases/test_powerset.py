import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.powerset import powerset
elif pytest.use_custom:
    from custom_python_programs.powerset import powerset
else:
    from python_programs.powerset import powerset


testdata = load_json_testcases(powerset.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_powerset(input_data, expected):
    assert set(map(tuple, powerset(*input_data))) == set(map(tuple, expected))
