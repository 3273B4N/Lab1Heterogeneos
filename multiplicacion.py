"""Matrix multiplication operation implementation."""

from operation_class import Operation


class Multiplicacion(Operation):
    """Child operation class that performs matrix multiplication."""

    def set_matrix(self, index: int, matrix):
        """Store a matrix in the given position.

        Args:
            index: Matrix position (0 for matrix A, 1 for matrix B).
            matrix: Matrix array to store.
        """
        self.matrices[index] = matrix

    def compute(self):
        """Compute the product of the stored matrices.

        Returns:
            The matrix result of A @ B.

        Raises:
            ValueError: If the matrices cannot be multiplied due to incompatible dimensions.
        """
        matriz_a = self.matrices[0]
        matriz_b = self.matrices[1]

        if matriz_a.shape[1] == matriz_b.shape[0]:
            return matriz_a @ matriz_b
        raise ValueError("Las dimensiones no coinciden")

    def clear(self):
        """Clear stored matrices."""
        self.matrices.clear()
