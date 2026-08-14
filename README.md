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

## Instructions for use

## Examples of how to use it
