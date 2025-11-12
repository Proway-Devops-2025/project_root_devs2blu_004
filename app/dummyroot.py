# dummy_math.py
"""
Módulo: dummy_math
Descrição:
    Este módulo contém funções fictícias usadas apenas para demonstração e testes.
    As funções aqui não têm propósito real em produção, servem como exemplo de código
    com documentação clara dentro do próprio arquivo.
"""

from typing import List


def average(numbers: List[float]) -> float:
    """
    Calcula a média aritmética de uma lista de números.

    Args:
        numbers (List[float]): lista contendo valores numéricos.

    Returns:
        float: média dos valores informados.

    Raises:
        ValueError: se a lista estiver vazia.
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")
    return sum(numbers) / len(numbers)


def add(a: float, b: float) -> float:
    """
    Soma dois números.

    Args:
        a (float): primeiro número.
        b (float): segundo número.

    Returns:
        float: resultado da soma de a + b.
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """
    Multiplica dois números.

    Args:
        a (float): primeiro número.
        b (float): segundo número.

    Returns:
        float: resultado da multiplicação de a * b.
    """
    return a * b


# Exemplo de uso prático (executa apenas se rodar diretamente este arquivo)
if __name__ == "__main__":
    nums = [4, 8, 15, 16, 23, 42]
    print("Lista:", nums)
    print("Média:", average(nums))
    print("Soma:", add(10, 5))
    print("Multiplicação:", multiply(3, 7))
