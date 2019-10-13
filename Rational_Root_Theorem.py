"""
a = leading coefficient
z = constant
"""

def calc(a, z, func):
    factorsA = [e for e in range(1, a + 1) if a % e == 0]
    factorsZ = [e for e in range(1, z + 1) if z % e == 0]
    tests = []
    for n in factorsA:
        for n2 in factorsZ:
            tests.append(n2/n)
            tests.append(-(n2/n))
    print("Roots of " + func + ":")
    print([t for t in set(tests) if eval(func.replace("x", "(" + str(t) + ")", func.count('x'))) == 0])
    print("")

#Tests
calc(2, 3, '2 * x**3 + 3 * x**2 + 2 * x + 3')
calc(1, 10, 'x**3 - 8 * x**2 + 17 * x - 10')
calc(1, 1, "x**3 - x**2 + 1")
calc(5, 5, "5 * x ** 3 + 29 * x**2 + 19 * x - 5")
calc(1, 64, "x**6 - 64")