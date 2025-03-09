from sympy import Sum, factorial, oo, symbols, E, N, pi, cos, sin, exp
from sympy.abc import k

x = symbols("x")


def power_series_exp(a, max_err=1e-3):
    f = x**k / factorial(k)
    total = 0
    i = 0
    max_iter = 100
    while True:
        total += f.subs({k: i, x: a}).evalf()
        err = abs(total - exp(a))
        print(f"{N(total)}, error = {N(err)}")
        if err < max_err or max_iter < i:
            break
        i += 1
    return total


def power_series_cos(a, max_err=1e-3):
    f = (-1) ** (k) * x ** (2 * k) / factorial(2 * k)
    total = 0
    i = 0
    max_iter = 100
    while True:
        total += f.subs({k: i, x: a}).evalf()
        err = abs(total - cos(a))
        print(f"{N(total)}, error = {N(err)}")
        if err < max_err or max_iter < i:
            break
        i += 1
    return total


def power_series_sin(a, max_err=1e-3):
    f = (-1) ** (k) * x ** (2 * k + 1) / factorial(2 * k + 1)
    total = 0
    i = 0
    max_iter = 100
    while True:
        total += f.subs({k: i, x: a}).evalf()
        err = abs(total - sin(a))
        print(f"{N(total)}, error = {N(err)}")
        if err < max_err or max_iter < i:
            break
        i += 1
    return total


def power_series_exp_test():
    power_series_exp(1)


def power_series_cos_test():
    power_series_cos(pi/2)


def power_series_sin_test():
    power_series_sin(pi/2)


# 测试场景一：指数函数（exp）
print("指数函数（exp）")
power_series_exp_test()
# 测试场景二：余弦函数（cos）
print("余弦函数（cos）")
power_series_cos_test()
# 测试场景三：正弦函数（sin）
print("正弦函数（sin）")
power_series_sin_test()
