# generate tests for matrix-vector-product function in matvec_multiply.py

# generate tests for dot-product function in matvec_multiply.py
import unittest

try:
    from bmi500.matvec_multiply import dot_product, matvec_multiply
except ImportError:
    from matvec_multiply import dot_product, matvec_multiply


class DotProductTests(unittest.TestCase):
    def test_dot_product_with_integers(self):
        self.assertEqual(dot_product([1, 2, 3], [4, 5, 6]), 32)

    def test_dot_product_with_floats(self):
        result = dot_product([0.5, 1.5], [2.0, 4.0])
        self.assertAlmostEqual(result, 7.0)

    def test_dot_product_rejects_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            dot_product([1, 2], [1])

    def test_dot_product_rejects_non_numeric_values(self):
        with self.assertRaises(TypeError):
            dot_product([1, "bad"], [2, 3])

    def test_dot_product_rejects_invalid_container_type(self):
        with self.assertRaises(TypeError):
            dot_product("12", [1, 2])


class MatVecMultiplyTests(unittest.TestCase):
    def test_matvec_multiply_returns_expected_values(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        vector = [7, 8, 9]
        self.assertEqual(matvec_multiply(matrix, vector), [50, 122])

    def test_matvec_multiply_returns_empty_list_for_empty_matrix(self):
        self.assertEqual(matvec_multiply([], [1, 2, 3]), [])

    def test_matvec_multiply_rejects_ragged_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5],
        ]
        with self.assertRaises(ValueError):
            matvec_multiply(matrix, [1, 2, 3])

    def test_matvec_multiply_rejects_vector_length_mismatch(self):
        matrix = [
            [1, 2],
            [3, 4],
        ]
        with self.assertRaises(ValueError):
            matvec_multiply(matrix, [1, 2, 3])

    def test_matvec_multiply_rejects_non_numeric_matrix_values(self):
        matrix = [
            [1, 2],
            [3, "bad"],
        ]
        with self.assertRaises(TypeError):
            matvec_multiply(matrix, [1, 2])

    def test_matvec_multiply_rejects_invalid_row_type(self):
        matrix = [
            [1, 2],
            "34",
        ]
        with self.assertRaises(TypeError):
            matvec_multiply(matrix, [1, 2])

    def test_matvec_multiply_rejects_invalid_vector_type(self):
        with self.assertRaises(TypeError):
            matvec_multiply([[1, 2], [3, 4]], "12")


if __name__ == "__main__":
    unittest.main()
