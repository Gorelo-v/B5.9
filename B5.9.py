
import time

def time_this(num_runs):
    def decorator(func):
        def wrap(param):
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func(param)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            return avg_time
        return wrap
    return decorator



@time_this(num_runs=10)
def f(param):
    for _ in range(param):
        pass

print(f(1000000))