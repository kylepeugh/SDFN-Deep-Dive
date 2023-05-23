#!/usr/bin/env python3
# import the random module 
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# create a random player subclass to return a random move 
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # add a score attribute
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        # to handle the ties correctly
        # check if the two moves are the same
        if move1 == move2:
            print("That was a tie, this round will be repeated")
            print(f"Player score is :{self.p1.score} || Random player score is: {self.p2.score}")
            self.play_round()
        # if they were not the same, let's see who win
        # I will indent the if statement
        else:
            if(beats(move1, move2)):
                # update the score
                self.p1.score += 1
                # fix the print statement to give more context
                print(f"Player score is :{self.p1.score} || Random player score is: {self.p2.score}")
            else:
                self.p2.score += 1
                # the same print statement
                print(f"Player score is :{self.p1.score} || Random player score is: {self.p2.score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    # change this from player to random player to test 
    game = Game(Player(), RandomPlayer())
    game.play_game()
