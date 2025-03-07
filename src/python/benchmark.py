import math
import statistics
import time


def square_1(x: float) -> float:
    return x**2


def square_2(x: int) -> float:
    return x * x


def square_3(x: int) -> float:
    return math.pow(x, 2)


def benchmark(ls_funcs: list[callable], *args, n_iter: int = 100, **kwargs):
    for func in ls_funcs:
        avg, std = average_runtime(func, n_iter, *args, **kwargs)
        print(f"# Average time for {func.__name__}: {avg:.4} ± {std:.4}.")


def func_time(fun: callable, *args, **kwargs) -> float:
    t1 = time.perf_counter()
    _ = fun(*args, **kwargs)
    t2 = time.perf_counter()
    return t2 - t1


def average_runtime(fun: callable, n_iter: int, *args, **kwargs) -> float:
    times = [func_time(fun, *args, **kwargs) for _ in range(n_iter)]
    avg = statistics.mean(times)
    std = statistics.stdev(times)
    return avg, std


if __name__ == "__main__":
    benchmark([square_1, square_2, square_3], 141412.510910, n_iter=1_000_000)
