import prompt
from random import randint

def its_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
       final = f'Congratulations, {name}!'
       random_number = randint(1, 30)
       print(f'Question: {random_number}')
       answer = prompt.string('Your answer: ')
       print(answer)
       if random_number % 2 == 0 and answer == 'yes':
          print('Correct!')
          count +=1
       elif random_number % 2 != 0 and answer == 'no':
          print('Correct!')
          count +=1
       elif random_number % 2 == 0 and answer == 'no':
          print(f'''"no" is wrong answer ;(. Correct answer was "yes".
Let's try again, {name}!''')
          count = 0
       elif random_number % 2 != 0 and answer == 'yes':
          print(f'''"yes" is wrong answer ;(. Correct answer was "no".
Let's try again, {name}!''')
          count = 0
       elif answer != 'no' or answer != 'yes':
          print(f'''{answer} is wrong answer ;(.
Let's try again, {name}!''')
    print(final)
