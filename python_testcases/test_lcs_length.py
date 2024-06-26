import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.lcs_length import lcs_length
elif pytest.use_custom:
    from custom_python_programs.lcs_length import lcs_length
else:
    from python_programs.lcs_length import lcs_length


testdata = load_json_testcases(lcs_length.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_lcs_length(input_data, expected):
    assert lcs_length(*input_data) == expected
