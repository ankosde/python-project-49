from random import randint
from random import choice


TASK = 'What is the result of the expression?'


def get_results():
    random_number = randint(20, 40)
    random_number1 = randint(1, 20)
    list = ['+', '-', '*']
    operazia = choice(list)
    true_answer = condition_check(random_number, random_number1, operazia)
    question = f'{random_number} {operazia} {random_number1}'
    return question, str(true_answer)


def condition_check(random_number, random_number1, operazia):
    if operazia == '-':
        rezult = random_number - random_number1
    elif operazia == '+':
        rezult = random_number + random_number1
    elif operazia == '*':
        rezult = random_number * random_number1
    return rezult

