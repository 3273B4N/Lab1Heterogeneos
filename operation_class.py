"""Base operation definitions for matrix computations."""

from abc import ABC, abstractmethod
import numpy as np


class Operation(ABC):
    """Abstract base class for matrix operations."""

    def __init__(self):
        """Initialize the operation with empty matrix storage."""
        self.matrices = {}

    @abstractmethod
    def set_matrix(self, index: int, matrix: np.ndarray):
        """Store a matrix for the operation.

        Args:
            index: Position in the operation (0 for matrix A, 1 for matrix B).
            matrix: Matrix array to store.
        """
        pass

    @abstractmethod
    def compute(self):
        """Compute the result of the operation.

        Returns:
            The result matrix for the operation.
        """
        pass

    @abstractmethod
    def clear(self):
        """Clear stored matrix state."""
        pass
