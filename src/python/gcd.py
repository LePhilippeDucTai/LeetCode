def gcd(n: int, p: int):
    if p > n:
        return gcd(p, n)
    if n % p == 0:
        return p
    return gcd(p, n % p)


def fibonacci(n):
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b


x = gcd(10, 15)
y = gcd(243, 225)
print(x)
print(y)
