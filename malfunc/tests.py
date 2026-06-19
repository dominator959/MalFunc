"""
test.py - Unit tests for the MalFunc library

Covers all 9 functions:
  ops.py   -> get_number, get_sum, get_mul, get_indices, vectorize_sum
  utils.py -> vectorize_mul, get_unique_order_list, get_flat, get_dtypes

Run with:
    python -m unittest test.py -v
or simply:
    python test.py
"""

import unittest
from unittest.mock import patch

import ops
import utils


class TestGetNumber(unittest.TestCase):
    """Tests for ops.get_number"""

    @patch("builtins.input", return_value="42")
    def test_valid_int(self, mock_input):
        self.assertEqual(ops.get_number("Enter:", to_int=True), 42)
        self.assertIsInstance(ops.get_number("Enter:", to_int=True), int)

    @patch("builtins.input", return_value="3.14")
    def test_valid_float(self, mock_input):
        self.assertEqual(ops.get_number("Enter:"), 3.14)
        self.assertIsInstance(ops.get_number("Enter:"), float)

    @patch("builtins.input", side_effect=["abc", "10"])
    def test_retries_on_invalid_then_succeeds(self, mock_input):
        # First call returns "abc" (invalid), loop should retry and
        # the second call returns "10" (valid).
        result = ops.get_number("Enter:", to_int=True)
        self.assertEqual(result, 10)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", return_value="7")
    def test_int_string_as_float_mode(self, mock_input):
        # to_int=False should still accept whole-number strings, as a float
        self.assertEqual(ops.get_number("Enter:"), 7.0)


class TestGetSum(unittest.TestCase):
    """Tests for ops.get_sum"""

    def test_flat_list(self):
        self.assertEqual(ops.get_sum([1, 2, 3]), [6])

    def test_ignores_non_numeric(self):
        self.assertEqual(ops.get_sum([1, "x", 2]), [3])

    def test_nested_list(self):
        # main level sum first via recursion order: nested appended before parent
        result = ops.get_sum([1, [2, 3], 4])
        self.assertEqual(result, [5, 5])  # [2,3]->5 appended first, then [1,4]->5

    def test_empty_list(self):
        self.assertEqual(ops.get_sum([]), [0])

    def test_deeply_nested(self):
        result = ops.get_sum([1, [2, [3, 4]]])
        # innermost [3,4]->7, then [2, ...]->2, then outer [1, ...]->1
        self.assertEqual(result, [7, 2, 1])


class TestGetIndices(unittest.TestCase):
    """Tests for ops.get_indices (moved here from utils.py)"""

    def test_flat_list(self):
        result = ops.get_indices(["a", "b"])
        self.assertEqual(
            result,
            [{"path": [0], "value": "a"}, {"path": [1], "value": "b"}],
        )

    def test_nested_list(self):
        data = [1, [2, 3]]
        result = ops.get_indices(data)
        expected = [
            {"path": [0], "value": 1},
            {"path": [1], "value": [2, 3]},
            {"path": [1, 0], "value": 2},
            {"path": [1, 1], "value": 3},
        ]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        self.assertEqual(ops.get_indices([]), [])


class TestGetMul(unittest.TestCase):
    """Tests for ops.get_mul"""

    def test_flat_list(self):
        self.assertEqual(ops.get_mul([2, 3, 4]), [24])

    def test_ignores_non_numeric(self):
        self.assertEqual(ops.get_mul([2, "x", 3]), [6])

    def test_nested_list(self):
        result = ops.get_mul([2, [3, 4]])
        # inner [3,4] -> 12 appended first, then outer [2, ...] -> 2
        self.assertEqual(result, [12, 2])

    def test_no_numeric_items_returns_zero(self):
        self.assertEqual(ops.get_mul(["a", "b"]), [0])

    def test_empty_list_returns_zero(self):
        self.assertEqual(ops.get_mul([]), [0])


class TestVectorizeSum(unittest.TestCase):
    """Tests for ops.vectorize_sum"""

    def test_simple_sum(self):
        self.assertEqual(ops.vectorize_sum([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_nested_sum(self):
        self.assertEqual(
            ops.vectorize_sum([1, [2, 3]], [10, [20, 30]]),
            [11, [22, 33]],
        )

    def test_unequal_length_raises(self):
        with self.assertRaises(ValueError):
            ops.vectorize_sum([1, 2], [1, 2, 3])

    def test_non_list_input_raises(self):
        with self.assertRaises(TypeError):
            ops.vectorize_sum(1, [1, 2])

    def test_mismatched_nesting_raises(self):
        with self.assertRaises(TypeError):
            ops.vectorize_sum([1, [2, 3]], [1, 2])

    def test_non_numeric_elements_raise(self):
        with self.assertRaises(TypeError):
            ops.vectorize_sum([1, "a"], [2, 3])


class TestVectorizeMul(unittest.TestCase):
    """Tests for utils.vectorize_mul"""

    def test_simple_mul(self):
        self.assertEqual(utils.vectorize_mul([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_nested_mul(self):
        self.assertEqual(
            utils.vectorize_mul([2, [3, 4]], [10, [5, 5]]),
            [20, [15, 20]],
        )

    def test_unequal_length_raises(self):
        with self.assertRaises(ValueError):
            utils.vectorize_mul([1, 2], [1])

    def test_non_list_input_raises(self):
        with self.assertRaises(TypeError):
            utils.vectorize_mul("ab", [1, 2])

    def test_mismatched_nesting_raises(self):
        with self.assertRaises(TypeError):
            utils.vectorize_mul([[1, 2]], [1])

    def test_non_numeric_elements_raise(self):
        with self.assertRaises(TypeError):
            utils.vectorize_mul([1, "a"], [2, 3])


class TestGetUniqueOrderList(unittest.TestCase):
    """Tests for utils.get_unique_order_list"""

    def test_removes_duplicates_preserves_order(self):
        self.assertEqual(
            utils.get_unique_order_list([3, 1, 3, 2, 1, 4]),
            [3, 1, 2, 4],
        )

    def test_no_duplicates(self):
        self.assertEqual(utils.get_unique_order_list([1, 2, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(utils.get_unique_order_list([]), [])

    def test_strings(self):
        self.assertEqual(
            utils.get_unique_order_list(["b", "a", "b", "c", "a"]),
            ["b", "a", "c"],
        )


class TestGetFlat(unittest.TestCase):
    """Tests for utils.get_flat"""

    def test_already_flat(self):
        self.assertEqual(utils.get_flat([1, 2, 3]), [1, 2, 3])

    def test_single_level_nesting(self):
        self.assertEqual(utils.get_flat([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_deep_nesting(self):
        self.assertEqual(
            utils.get_flat([1, [2, [3, [4, 5]], 6], 7]),
            [1, 2, 3, 4, 5, 6, 7],
        )

    def test_empty_list(self):
        self.assertEqual(utils.get_flat([]), [])

    def test_mixed_types_preserved(self):
        self.assertEqual(
            utils.get_flat([1, ["a", [2.5, "b"]], None]),
            [1, "a", 2.5, "b", None],
        )


class TestGetDtypes(unittest.TestCase):
    """Tests for utils.get_dtypes"""

    def test_mixed_types(self):
        result = utils.get_dtypes([1, "a", 2.5, "b", 3])
        self.assertEqual(result, {"int": 2, "str": 2, "float": 1})

    def test_empty_list(self):
        self.assertEqual(utils.get_dtypes([]), {})

    def test_single_type(self):
        self.assertEqual(utils.get_dtypes([1, 2, 3]), {"int": 3})

    def test_includes_lists_and_none(self):
        result = utils.get_dtypes([1, [2, 3], None, "x"])
        self.assertEqual(result, {"int": 1, "list": 1, "NoneType": 1, "str": 1})


if __name__ == "__main__":
    unittest.main(verbosity=2)