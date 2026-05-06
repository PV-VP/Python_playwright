import random
import string


def generate_task_name():
    return  "Task " + "".join(random.choices(string.ascii_letters, k=16))

def generate_random_name():
    return  "Meeting " + "".join(random.choices(string.ascii_letters, k=6))

def generate_random_fill():
    return  "".join(random.choices(string.ascii_letters, k=80))

def generate_random_digit():
    return str((random.randint(1, 10000)))

def generate_random_fill_20_symbols():
    return  "".join(random.choices(string.ascii_letters, k=20))

def generate_fibonacci():
    fib = [1, 1]

    while fib[-1] < 21:
        fib.append(fib[-1] + fib[-2])

    fib = [x for x in fib if x <= 21]
    return str(random.choice(fib))
