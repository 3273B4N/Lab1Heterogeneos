from operation_class import Operation
import numpy as np


class Inverse(Operation):
    """Class to compute the inverse of a matrix."""

    def set_matrix(self, index: int, matrix: np.ndarray):
        """Configures the matrix.

        Args:
            index: Matrix position.
            matrix: Floating point matrix to store.
        """
        self.matrixes[index] = matrix

    def compute(self):
        """Computes the inverse of the matrix."""

        if not self.matrixes:
            raise ValueError("No matrices have been set.")

        if 0 not in self.matrixes:
            raise ValueError("Matrix at index 0 has not been set.")

        first_matrix = self.matrixes[0]

        if first_matrix.shape[0] != first_matrix.shape[1]:
            raise ValueError(
                "Matrix must be square to compute inverse."
            )

        determinant = np.linalg.det(first_matrix)

        if np.isclose(determinant, 0):
            raise ValueError(
                "Matrix is singular and cannot be inverted."
            )

        return np.linalg.inv(first_matrix)

    def clear(self):
        """Clears the internal state."""
        self.matrixes.clear()
