"""Matrix addition operation implementation."""

from operation_class import Operation
import numpy as np


class Suma(Operation):
    """Child operation class that performs matrix addition."""

    def set_matrix(self, index: int, matrix: np.ndarray):
        """Store a matrix in the given position.

        Args:
            index: Matrix position (0 for matrix A, 1 for matrix B).
            matrix: Matrix array to store.
        """
        self.matrices[index] = matrix

    def compute(self):
        """Compute the sum of the stored matrices.

        Returns:
            The matrix result of A + B.

        Raises:
            ValueError: If the two matrices do not have identical dimensions.
        """
        matriz_a = self.matrices[0]
        matriz_b = self.matrices[1]

        if matriz_a.shape == matriz_b.shape:
            return matriz_a + matriz_b
        raise ValueError("Las matrices no tienen las misma dimensiones")

    def clear(self):
        """Clear stored matrices."""
        self.matrices.clear()
