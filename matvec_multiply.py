import random
from numbers import Real


def _is_numeric(value):
    """Return True when value is a real number but not a boolean."""
    return isinstance(value, Real) and not isinstance(value, bool)

# create a function to compute the dot product of two vectors using a for loop
# add comments for the selected function
def dot_product(vector_a, vector_b):
    """Compute the dot product of two equally sized numeric vectors."""
    if not isinstance(vector_a, (list, tuple)) or not isinstance(vector_b, (list, tuple)):
        raise TypeError("dot_product expects both inputs to be lists or tuples.")

    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length.")

    total = 0
    for index, (value_a, value_b) in enumerate(zip(vector_a, vector_b)):
        if not _is_numeric(value_a) or not _is_numeric(value_b):
            raise TypeError(
                f"Vectors must contain only real numeric values. Invalid value at index {index}."
            )
        total += value_a * value_b

    return total



# create a function to compute the matrix-vector product using the dot_product function
# add comments for the selected function
def matvec_multiply(matrix, vector):
    """Multiply a matrix by a vector and return the resulting vector."""
    if not isinstance(matrix, (list, tuple)):
        raise TypeError("Matrix must be a list or tuple of rows.")

    if not isinstance(vector, (list, tuple)):
        raise TypeError("Vector must be a list or tuple.")

    if len(matrix) == 0:
        return []

    expected_row_length = len(vector)
    result = []

    for row_index, row in enumerate(matrix):
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Matrix row {row_index} must be a list or tuple.")

        if len(row) != expected_row_length:
            raise ValueError(
                "Each matrix row must have the same length as the vector."
            )

        # Reuse dot_product so that vector validation stays consistent.
        result.append(dot_product(row, vector))

    return result



# create a main function to test the matrix-vector product function using randomly generated data of size 1000x1000
# add comments for the selected function
def main():
    """Generate random data and run a simple matrix-vector multiplication demo."""
    size = 1000

    # Build a square matrix and matching vector so the multiplication is valid.
    matrix = [[random.random() for _ in range(size)] for _ in range(size)]
    vector = [random.random() for _ in range(size)]

    product = matvec_multiply(matrix, vector)
    print(f"Computed product for a {size}x{size} matrix and length-{size} vector.")
    print(f"Result length: {len(product)}")
    print(f"First five values: {product[:5]}")


if __name__ == "__main__":
    main()
