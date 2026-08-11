from abc import ABC, abstractmethod
import numpy as np


class Operation(ABC):
    """Abstract father class,
    inherits to other operacion classes"""

    def __init__(self):
        """Initializes the matrixes atribute,
        dictionary to store matrixes states"""
        self.matrixes = {}

    @abstractmethod
    def set_matrix(self, index: int, matrix: np.ndarray):
        """Configures the matrix
        Args:
            index: matrix position
            matrix: floating point matrix to store in
        """
        pass

    @abstractmethod
    def compute(self):
        """Executes operations on the matrixes
        returns the result of the operation"""
        pass

    @abstractmethod
    def clear(self):
        """Clears the internal state"""
        pass
