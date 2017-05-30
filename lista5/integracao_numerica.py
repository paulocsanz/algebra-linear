def integracao_numerica(func, a, b, N):
    A = 0
    delta_x = (b - a)/(N - 1)
    for i in range(N):
        x = a
        a += delta_x
        next_x = a
        A += (func(next_x) + func(x)) * delta_x / 2
    return A

if __name__ == "__main__":
    from math import e
    f = lambda x: e ** (-x ** 2)
    print(integracao_numerica(f, 0, 1, 10000))
