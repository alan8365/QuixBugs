import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.gcd import gcd
elif pytest.use_custom:
    from custom_python_programs.gcd import gcd
else:
    from python_programs.gcd import gcd


testdata = load_json_testcases(gcd.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_gcd(input_data, expected):
    assert gcd(*input_data) == expected
