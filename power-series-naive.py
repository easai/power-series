from sympy import Sum, factorial, oo, symbols, E, N, pi, cos, sin
from sympy.abc import k

x = symbols("x")


def power_series_exp(x, n):
    f = 0
    for i in range(n+1):
        f += x**i / factorial(i)
        err = abs(f - E)
        print(f"{N(f)}, error = {N(err)}")
    return f


def power_series_cos(x, n):
    f = 0
    for i in range(n):
        if i % 2 == 0:
            if i % 4 == 0:
                f += x**i / factorial(i)
            else:
                f -= x**i / factorial(i)
            err = abs(f - cos(x))
            print(f"{N(f)}, error = {N(err)}")
    return f


def power_series_sin(x, n):
    f = 0
    for i in range(n):
        if i % 2 != 0:
            if i % 4 == 1:
                f += x**i / factorial(i)
            else:
                f -= x**i / factorial(i)
            err = abs(f - sin(x))
            print(f"{N(f)} error = {N(err)}")
    return f


def power_series_exp_test(n):
    f = power_series_exp(1, n)


def power_series_cos_test(n):
    f = power_series_cos(pi/2, n)


def power_series_sin_test(n):
    f = power_series_sin(pi/2, n)


# 测试场景一：指数函数（exp）
print("指数函数（exp）")
power_series_exp_test(5)
# 测试场景二：正弦函数（sin）
print("正弦函数（sin）")
power_series_cos_test(5)
# 测试场景三：余弦函数（cos）
print("余弦函数（cos）")
power_series_sin_test(5)