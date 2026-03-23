import random

def random_mail():
    left_num = random.randint(0, 1000)
    right_num = random.randint(0, 1000)
    return f"random{left_num}@test{right_num}.com"

