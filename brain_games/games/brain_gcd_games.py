from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def get_results():
    random_number = randint(1, 100)
    random_number1 = randint(1, 100)
    min_num = min(random_number, random_number1)
    true_answer = condition_check(random_number, random_number1, min_num)
    question = f'{random_number} {random_number1}'
    return question, str(true_answer)


def condition_check(random_number, random_number1, min_num):
    count = 0
    for i in range(1, min_num + 1):
       if random_number % i == 0 and random_number1 % i == 0:
          count = i
    return count

