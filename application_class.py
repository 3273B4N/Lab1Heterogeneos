import numpy as np

from operation_class import Operation
from suma import Sum
from multiplicacion import Multiplication
from inverse import Inverse
from determinant import Determinant


class Application:
    """Represents the matrix calculator app

    Contains the supported operations and
    coordinates the execution on each operation:
    recives the operation name and matrixes from
    the CLI interface and uses the right operations
    Returns the result of the operation

    Attributes:
        operations (dict[str, Operation]):
        Maps the operation name to its correct operation instance.
    """

    def __init__(self):
        """Initializes the supported operations dictionary"""
        self.operations: dict[str, Operation] = {
            "sum": Sum(),
            "multiplication": Multiplication(),
            "inverse": Inverse(),
            "determinant": Determinant(),
        }

    def execute(self, operation_name: str, matrixes: list):
        """Executes the correct operation on the given matrixes

        Args:
            operation_name: Name of the operation to execute,
            must exist as a key in self.operations
            matrixes: List of matrixes, in order acording to
            the index

        Returns:
            The operation resulta as a numpy array

        Raises:
            ValueError: If operation is not supported
        """
        if operation_name not in self.operations:
            raise ValueError(
                f"Operation '{operation_name}' not supported."
            )

        operation = self.operations[operation_name]
        operation.clear()

        """Creates the numpy array that can be computed
        """

        for index, matrix in enumerate(matrixes):
            matrix_np = np.array(matrix, dtype=float)
            operation.set_matrix(index, matrix_np)

        """Computes the operation result"""

        return operation.compute()
