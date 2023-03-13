#!/usr/bin/env python3

from brain_games.games import brain_gcd_games
from brain_games.logic.logic_game import running_game


def main():
    running_game(brain_gcd_games)


if __name__ == '__main__':
    main()
