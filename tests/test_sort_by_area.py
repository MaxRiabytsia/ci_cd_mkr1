import pytest
import os

from main import sort_by_area, read_data


@pytest.mark.parametrize('file_name, expected', [
    ["data.txt", [['poland', '400000', '42.32'], ['ukraine', '603700', '43.79'], ['usa', '20000000', '311.56']]],
    ["data2.txt", [['spain', '400000', '66.67'], ['germany', '440000', '68.37'], ['france', '590000', '70.21']]],
])
def test_sort_by_area(file_name, expected):
    data = read_data(os.path.join("..", file_name))
    assert sort_by_area(data) == expected
