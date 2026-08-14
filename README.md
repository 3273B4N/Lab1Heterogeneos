# Lab 1

**Members**
- Gael Agüero Carrillo
- Luis Diego García Rojas
- Jennifer Porras Rojas
- Esteban Sanchez Acevedo

**Introducción a la computación heterogénea**

**Professor: Luis Leon Vega**

## Project description

A minimal processor for a matrix calculator is implemented in Python; it accepts matrices in JSON format, represented as two-dimensional arrays of floating-point numbers. This calculator supports four fundamental operations: addition, multiplication, determinant, and inverse.

The system is built using the Interface-Adapter architectural pattern, where each mathematical operation is implemented in its own class and all share a common structure ('Operation'), making it easy to add new operations without affecting the system. The 'App' class stores all available operations in a dictionary, separating the calculation logic from the user interface.

Interaction with the calculator takes place via a command-line interface (CLI) built with Typer, and the project uses UV as the build and dependency management system.

## Design diagram

## Installation instructions

### Requirements

- Python installed
- [UV] installed as the dependency management system

### Installation steps

1. Clone the repository:

```bash
git clone <repository-url>
cd <Lab1Heterogeneos>
``` 
2. Move to the branch called develop

```bash
git checkout develop
```

3. Install the project dependencies with UV:

```bash
uv sync
```
This command automatically creates a virtual environment and installs all necessary dependencies as defined in `pyproject.toml` and `uv.lock`.

4. Verify that the installation was successful:

```bash
uv run python cli.py --help
```
If the help displaying the available operations appears, the installation
completed successfully.

## Instructions for use

The calculator runs from the command line using Typer, with each operation invoked as a separate command that specifies the JSON file containing the matrices to be processed.

### View available commands

```bash
uv run python cli.py --help
```

### Available commands

| Operation | Command |
|---|---|
| Addition | `sum` |
| Multiplication | `mul` |
| Investment | `inv` |
| Determinant | `det` |

### Syntax for using the calculator

```bash
uv run python cli.py <command> <file-name.json>
```

### Input JSON file format

```json
{
  "matrixA": {
    "rows": 2,
    "cols": 3,
    "data": [
      [1.25, 2.50, 3.75],
      [4.00, 5.10, 6.20]
    ]
  },
  "matrixB": {
    "rows": 3,
    "cols": 2,
    "data": [
      [10.0, 11.0],
      [12.0, 13.0],
      [14.0, 15.0]
    ]
  }
}
```

## Examples of how to use it
