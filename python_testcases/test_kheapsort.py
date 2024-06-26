import pytest
from load_testdata import load_json_testcases

if pytest.use_correct:
    from correct_python_programs.kheapsort import kheapsort
elif pytest.use_custom:
    from custom_python_programs.kheapsort import kheapsort
else:
    from python_programs.kheapsort import kheapsort


testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
@pytest.mark.timeout(2)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
