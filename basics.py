
from functools import wraps
from time import perf_counter


def log_function_call(func):
    """Print a message before and after a function runs."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result

    return wrapper


def measure_time(func):
    """Measure how long a function takes to execute."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"Execution time: {elapsed:.6f} seconds")
        return result

    return wrapper


@log_function_call
@measure_time
def calculate_sum(n):
    """Return the sum of numbers from 1 to n."""
    return sum(range(1, n + 1))


def main():
    number = 100_000
    result = calculate_sum(number)
    print(f"Sum from 1 to {number}: {result}")


if __name__ == "__main__":
    main()
