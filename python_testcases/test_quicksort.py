import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.quicksort import quicksort
elif pytest.use_custom:
    from custom_python_programs.quicksort import quicksort
else:
    from python_programs.quicksort import quicksort


testdata = load_json_testcases(quicksort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_quicksort(input_data, expected):
    assert quicksort(*input_data) == expected
