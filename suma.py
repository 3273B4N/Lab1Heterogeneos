"""Matrix addition operation implementation."""

from operation_class import Operation
import numpy as np


class Sum(Operation):
    """Child operation class that performs matrix addition."""

    def set_matrix(self, index: int, matrix: np.ndarray):
        """Store a matrix in the given position.

        Args:
            index: Matrix position (0 for matrix A, 1 for matrix B).
            matrix: Matrix array to store.
        """
        self.matrixes[index] = matrix

    def compute(self):
        """Compute the sum of the stored matrices.

        Returns:
            The matrix result of A + B.

        Raises:
            ValueError: If the two matrices do not have identical dimensions.
        """
        matrix_a = self.matrixes[0]
        matrix_b = self.matrixes[1]

        if matrix_a.shape == matrix_b.shape:
            return matrix_a + matrix_b
        raise ValueError("Matrixes do not match dimensions")

    def clear(self):
        """Clear stored matrices."""
        self.matrixes.clear()
