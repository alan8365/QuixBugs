import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.kth import kth
elif pytest.use_custom:
    from custom_python_programs.kth import kth
else:
    from python_programs.kth import kth


testdata = load_json_testcases(kth.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_kth(input_data, expected):
    assert kth(*input_data) == expected
