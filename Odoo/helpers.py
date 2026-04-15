import random
import string

def generate_task_name():
    return  "Task " + "".join(random.choices(string.ascii_letters, k=16))  # рандомні данні для назви задачі
def generate_random_name():
    return  "Meeting " + "".join(random.choices(string.ascii_letters, k=6))  # рандомні данні для назви зустрічі
def generate_random_fill():
    return  "".join(random.choices(string.ascii_letters, k=80))  # рандомні данні для опису зустрічі
