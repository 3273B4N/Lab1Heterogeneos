from clase_padre_Operacion import Operacion
import numpy as np


class Suma(Operacion):
    """Clase hija que realiza la suma"""

    def set_matrix(self, index, matrix):
        """guarda la matriz en la posición indicada
           es 0 para la matriz A y 1 para la matriz B"""
        self.matrices[index] = matrix

    def compute(self):
        """Ejecuta la operación suma sobre las matrices A y B
            Si las matrices A y B tienen las mismas dimensiones,
            se realiza la suma"""
        matriz_a = self.matrices[0]
        matriz_b = self. matrices[1]

        if matriz_a.shape == matriz_b.shape:
            suma = matriz_a + matriz_b
        else:
            raise ValueError("Las matrices no tienen las misma dimensiones")
        return suma

    def Clear(self):
        self.matrices.clear()
