# RatiRoot-Theorem
This is an algorithm that can calculate the rational roots of a function. It uses the leading coefficient, constant, and expression as parameters.

Examples:
```python
calc(2, 3, '2 * x**3 + 3 * x**2 + 2 * x + 3') = [-1.5]
calc(1, 10, 'x**3 - 8 * x**2 + 17 * x - 10') = [1.0, 2.0, 5.0]
calc(1, 1, "x**3 - x**2 + 1") = []
calc(5, 5, "5 * x ** 3 + 29 * x**2 + 19 * x - 5") = [0.2, -5.0, -1.0]
calc(1, 64, "x**6 - 64") = [2.0, -2.0]
```
