#!/usr/bin/env python3

import prompt
from brain_games.games import brain_progression_games
from brain_games.logic.logic_game import running_game


def main():
    running_game(brain_progression_games)


if __name__ == '__main__':
    main()
