def factorial (n):
    return 1 if n == 0 else n * factorial(n - 1)

def sumatoria(*elem: int):
    suma = 0
    for e in elem:
        suma += e
    
    return suma