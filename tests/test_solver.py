import pytest

from src.solver import ValuableObject, solve

class TestSolver:
    def test_simple(self):
        test_obj = [
            ValuableObject(value=3, weight=2, id=1),
            ValuableObject(value=4, weight=2, id=2),
            ValuableObject(value=7, weight=6, id=3),
            ValuableObject(value=3, weight=5, id=4)
        ]
        expected_ids = {2, 3}
        res = solve(test_obj, 8)
        assert expected_ids == set(obj.id for obj in res)

    def test_no_solution(self):
        test_obj = [
            ValuableObject(value=3, weight=5, id=1),
            ValuableObject(value=4, weight=7, id=2)
        ]
        res = solve(test_obj, 1)
        assert len(res) == 0

    def test_no_obj(self):
        assert len(solve([], 10)) == 0