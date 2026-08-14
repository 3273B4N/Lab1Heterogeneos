"""CLI entry points for matrix operations."""

import json
import typer
from application_class import Application

# TODO: reemplazar app por el nombre del archivo de la app y
# Aplicacion por el nombre de la clase de la aplicacion
# dentro del archivo de aplicacion

app = typer.Typer(help="Calculador de matrices por CLI")
aplication = Application()


def load_json(ruta: str) -> dict:
    """Load matrix data from a JSON file.

    Args:
        ruta: Path to the JSON file containing matrix definitions.

    Returns:
        Parsed JSON content as a dictionary.
    """
    with open(ruta, "r") as matrix_file:
        return json.load(matrix_file)


@app.command()
def sum(matrix_file: str):
    """Execute matrix addition from JSON input.

    Args:
        matrix_file: Path to a JSON file containing
        "matrixA" and "matrixB" entries.
    """
    data = load_json(matrix_file)
    resultado = aplication.execute("sum", [data["matrixA"]["data"],
                                           data["matrixB"]["data"]])
    print(f"El resultado de la operación es: {resultado}")


@app.command()
def mul(matrix_file: str):
    """Execute matrix multiplication from JSON input.

    Args:
        matrix_file: Path to a JSON file containing
        "matrixA" and "matrixB" entries.
    """
    data = load_json(matrix_file)
    resultado = aplication.execute("multiplication", [data["matrixA"]["data"],
                                                      data["matrixB"]["data"]])
    print(f"El resultado de la operación es: {resultado}")


@app.command()
def inv(matrix_file: str):
    """Execute matrix inversion from JSON input.

    Args:
        matrix_file: Path to a JSON file containing "matrixA" data.
    """
    data = load_json(matrix_file)
    resultado = aplication.execute("inverse", [data["matrixA"]["data"]])
    print(f"El resultado de la operación es: {resultado}")


@app.command()
def det(matrix_file: str):
    """Execute matrix determinant from JSON input.

    Args:
        matrix_file: Path to a JSON file containing "matrixA" data.
    """
    data = load_json(matrix_file)
    resultado = aplication.execute("determinant", [data["matrixA"]["data"]])
    print(f"El resultado de la operación es: {resultado}")


if __name__ == "__main__":
    app()
