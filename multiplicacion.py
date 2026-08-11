from clase_padre_Operacion import Operacion


class Multiplicacion(Operacion):
    """Clase hija que realiza la multiplicación"""

    def set_matrix(self, index, matrix):
        """guarda la matriz en la posición indicada
           es 0 para la matriz A y 1 para la matriz B"""
        self.matrices[index] = matrix

    def compute(self):
        """
        Ejecuta la operación multiplicación sobre las
        matrices A y B
        Si las dimensiones de las columnas de A y las filas de B
        son iguales, la multiplicación se realiza
        """
        matriz_a = self.matrices[0]
        matriz_b = self. matrices[1]

        if matriz_a.shape[1] == matriz_b.shape[0]:
            suma = matriz_a @ matriz_b
        else:
            raise ValueError(
                "Las dimensiones no coinciden")
        return suma

    def Clear(self):
        """Vacía el dicccionario self.matrices"""
        self.matrices.clear()
