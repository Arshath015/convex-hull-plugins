import pytest
from plugins.basic_plugin import BasicPlugin

@pytest.mark.parametrize("points, expected_hull", [
    ([(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)],
     [(0, 0), (0, 3), (4, 4), (3, 1)]),
    ([(1, 1), (2, 2), (3, 3)], [(1, 1), (2, 2), (3, 3)]),
    ([(0, 0)], [(0, 0)])
])
def test_convex_hull(points, expected_hull):
    assert BasicPlugin.convex_hull(points) == expected_hull
