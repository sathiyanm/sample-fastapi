# # # content of test_sample.py
# # def inc(x):
# #     return x + 1


# # def test_answer():
# #     assert inc(3) == 4

# # content of test_expectation.py
# import pytest


# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

# @pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
# class TestClass:
#     def test_simple_case(self, n, expected):
#         assert n + 1 == expected

#     def test_weird_simple_case(self, n, expected):
#         assert (n * 1) + 1 == expected

# @pytest.mark.parametrize(
#     "test_input,expected",
#     [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
# )
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected