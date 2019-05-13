"""Test for 3 d surface area"""
from .. import three_d_surface_area

def test_solution():
    "test"
    t_w = three_d_surface_area.ThreeDSurfaceArea()
    grid = [
        [1, 3, 4],
        [2, 2, 3],
        [1, 2, 4]
    ]
    assert t_w.solution(grid) == 60
