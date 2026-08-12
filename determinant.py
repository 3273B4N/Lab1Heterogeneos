from operation_class import Operation
import numpy as np

class Determinant(Operation):
    """Class to compute the determinant of a matrix"""

    def set_matrix(self, index: int, matrix: np.ndarray):
        """Configures the matrix
        Args:
            index: matrix position
            matrix: floating point matrix to store in
        """
        self.matrixes[index] = matrix

    def compute(self):
        """Executes operations on the matrixes
        returns the result of the operation"""
        if not self.matrixes:
            raise ValueError("No matrices have been set.")
        
        if 0 not in self.matrixes:
            raise ValueError("Matrix at index 0 has not been set.")
    
        # Assuming we want to compute the determinant of the first matrix set
        first_matrix = self.matrixes[0]

        if first_matrix.shape[0] != first_matrix.shape[1]:
            raise ValueError("Matrix must be square to compute determinant.")
        return np.linalg.det(first_matrix)

    def clear(self):
        """Clears the internal state"""
        self.matrixes.clear()