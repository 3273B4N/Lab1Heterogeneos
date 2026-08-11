from abc import ABC, abstractmethod
import numpy as np


class Operacion(ABC):
    """Clase abstracta padre,
    hereda a las otras operaciones"""

    def __init__(self):
        """Inicializa el atributo de matrices,
        diccionario para guardar matrices
        (sujeto a cambios)"""
        self.matrices = {}

    @abstractmethod
    def set_matrix(self, index: int, matrix: np.ndarray):
        """Configura la matriz en la posición indicada
        Args:
            index: Posición de la matriz
            matrix: Matriz de punto flotante a almacenar
        """
        pass

    @abstractmethod
    def compute(self):
        """Ejecuta la operación sobre las matrices cargadas
        retorna el resultado de la operación"""
        pass

    @abstractmethod
    def clear(self):
        """Limpia el estado interno"""
        pass
