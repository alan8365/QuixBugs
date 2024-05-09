import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.subsequences import subsequences
elif pytest.use_custom:
    from custom_python_programs.subsequences import subsequences
else:
    from python_programs.subsequences import subsequences


testdata = load_json_testcases(subsequences.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_subsequences(input_data, expected):
    result = subsequences(*input_data) 
    # result = {tuple(i) for i in result}

    # expected = {tuple(i) for i in expected}
    
    assert result == expected
