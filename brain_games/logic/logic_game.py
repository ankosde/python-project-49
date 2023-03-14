import prompt


ROUNDS = 3


def running_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    for _ in range(ROUNDS):
        final = f'Congratulations, {name}!'
        question, true_answer = game.get_results()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        print(answer)
        if answer == true_answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer"
                  f"was {true_answer}. \nLet's try again, {name}!")
            break
    else:
        print(final)

