import multiprocessing as mp


def foo(q):
    return q**2


if __name__ == '__main__':
    for q in range(1000):
        foo(q)
