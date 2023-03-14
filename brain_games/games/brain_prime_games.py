from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_results():
    question = randint(2, 100)
    true_answer = 'yes' if condition_check(question) else 'no'
    return question, true_answer


def condition_check(question):
    count = 0
    for i in range(2, question // 2):
        if question % i == 0:
            count += 1
    if count == 0:
        return True

