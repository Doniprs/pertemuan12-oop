import math
# Doni Perdana siringoringo
# kelas TI22B1


def a(n): return lambda x: x**n


lambdaA = a(3)
print(lambdaA(5))


def b(i, j):
    return lambda x, y: math.sqrt(x**i + y**j)


lambdaB = b(5, 1)
print(lambdaB(4, 2))


def c(*args):
    return lambda *params: sum(args) / len(params)


lambdaC = c(2, 2, 3, 4, 4)
print(lambdaC(4, 4, 4))


def d(firstname):
    return lambda *lastname: "".join(set(firstname)) + "".join(set(lastname))


lambdaD = d("Doni")
print(lambdaD("Perdana", "Siringoringo"))
