from __future__ import annotations
from typing import Union
from math import gcd

Number = Union[int, float, "Fraction"]

class Fraction:
    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        common = gcd(numerator, denominator)
        self._numerator = numerator // common
        self._denominator = denominator // common

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    def __add__(self, other: Number) -> Fraction:
        other = self._ensure_fraction(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other: Number) -> Fraction:
        other = self._ensure_fraction(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other: Number) -> Fraction:
        other = self._ensure_fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: Number) -> Fraction:
        other = self._ensure_fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero.")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other: Number) -> bool:
        other = self._ensure_fraction(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other: Number) -> bool:
        other = self._ensure_fraction(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: Number) -> bool:
        return self < other or self == other

    def __gt__(self, other: Number) -> bool:
        return not self <= other

    def __ge__(self, other: Number) -> bool:
        return not self < other

    def __ne__(self, other: Number) -> bool:
        return not self == other

    def __float__(self) -> float:
        return self.numerator / self.denominator

    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def _ensure_fraction(self, value: Number) -> Fraction:
        if isinstance(value, Fraction):
            return value
        elif isinstance(value, int):
            return Fraction(value)
        elif isinstance(value, float):
            # Convert float to fraction (approximate)
            from fractions import Fraction as StdFraction
            std_frac = StdFraction(value).limit_denominator()
            return Fraction(std_frac.numerator, std_frac.denominator)
        else:
            raise TypeError(f"Unsupported type: {type(value)}")