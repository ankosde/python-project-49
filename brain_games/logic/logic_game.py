import prompt


def running_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.TASK)
    count = 0
    while count < 3:
       final = f'Congratulations, {name}!'

       question, true_answer = game.get_results()
       print(f'Question: {question}')
       answer = prompt.string('Your answer: ')
       print(answer)
       if answer == true_answer:
          print('Correct!')
          count +=1
       else:
          print(f'{answer} is wrong answer ;(. Correct answer was {true_answer}.')
          print(f'''Let's try again, {name}!''')
          count = 0
          break
    print(final)
