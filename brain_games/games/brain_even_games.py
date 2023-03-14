from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_results():
    question = randint(1, 30)
    true_answer = 'yes' if condition_check(question) else 'no'
    return question, true_answer


def condition_check(question):
    if question % 2 == 0:
       return True
    else:
       return False

