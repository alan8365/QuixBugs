import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.mergesort import mergesort
elif pytest.use_custom:
    from custom_python_programs.mergesort import mergesort
else:
    from python_programs.mergesort import mergesort


testdata = load_json_testcases(mergesort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_mergesort(input_data, expected):
    assert mergesort(*input_data) == expected
