import prompt
import random


TASK = 'What number is missing in the progression?'

def get_results():
    min_num = random.randint(1, 8)
    max_num = random.randint(45, 57)
    random_step = random.randint(2, 5)
    subsequence = condition_check(min_num, max_num, random_step)
    random_index = random.randint(1, 10)
    true_answer = str(subsequence[random_index])
    subsequence[random_index] = '..'
    question = ' '.join(map(str, subsequence[0:11]))
    return question, true_answer

def condition_check(min_num, max_num, random_step):
    subsequence = []
    for i in range(min_num, max_num, random_step):
       subsequence.append(i)
    return subsequence
