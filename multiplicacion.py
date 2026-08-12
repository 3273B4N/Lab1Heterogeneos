"""Matrix multiplication operation implementation."""

from operation_class import Operation


class Multiplication(Operation):
    """Child operation class that performs matrix multiplication."""

    def set_matrix(self, index: int, matrix):
        """Store a matrix in the given position.

        Args:
            index: Matrix position (0 for matrix A, 1 for matrix B).
            matrix: Matrix array to store.
        """
        self.matrixes[index] = matrix

    def compute(self):
        """Compute the product of the stored matrices.

        Returns:
            The matrix result of A @ B.

        Raises:
            ValueError: If the matrices cannot be multiplied due to incompatible dimensions.
        """
        matrix_a = self.matrixes[0]
        matrix_b = self.matrixes[1]

        if matrix_a.shape[1] == matrix_b.shape[0]:
            return matrix_a @ matrix_b
        raise ValueError("Matrixes do not match dimensions")

    def clear(self):
        """Clear stored matrices."""
        self.matrices.clear()
