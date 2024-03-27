import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.find_first_in_sorted import find_first_in_sorted
elif pytest.use_custom:
    from custom_python_programs.find_first_in_sorted import find_first_in_sorted
else:
    from python_programs.find_first_in_sorted import find_first_in_sorted


testdata = load_json_testcases(find_first_in_sorted.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_find_first_in_sorted(input_data, expected):
    assert find_first_in_sorted(*input_data) == expected
