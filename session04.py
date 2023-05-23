import random

# declaring the moves as a global variable
moves = ['rock', 'paper', 'scissors']

# the parent class for all players
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# the rules that manage the gameplay
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# -----------------------------------Random Player ------------------
# create a random player subclass to return a random move 
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass

# ---------------------------------Human Player ---------------------
# to create a subclass for the human player
# we can use more one approach
class HumanPlayer(Player):
    def move(self):
        choice = input("Rock, Paper , or Scissors?")
        if choice.lower() in moves:
            return choice
        else:
            print("This is an invalid input")
            return self.move()

    def learn(self, my_move, their_move):
        pass
# another approach
# class HumanPlayer(Player):
#     def move(self):
#         choice = input("Choose your move, R for rock,"
#                        " P for paper or S for scissors?\n")
#         if choice == 'S' or choice == 's' or choice == 'scissors':
#             return 'scissors'
#         elif choice == 'P' or choice == 'p' or choice == 'paper':
#             return 'paper'
#         if choice == 'R' or choice == 'r' or choice == 'rock':
#             return 'rock'
#         else:
#             print("This is an invalid input")
#             return self.move()

#     def learn(self, my_move, their_move):
#         pass

# -----------------------------------reflect player ------------------------
# Now, in this subclass we have to find a way to reflect the human player moves
# to do so, we have to collect the player moves but in the first round
# when there is no input yet, we have to return something
# but at first how to make sure if this is the first round
class ReflectPlayer(Player):
    def move(self):
        # using the self object __dict__ to check if this was the first round
        # if the __dict__ contains my_move, that means this is not the first round
        # and the learn method has been called before
        if self.__dict__.keys().__contains__("my_move"):
            return self.my_move
        else:
            return random.choice(moves)
        
    def learn(self, my_move, their_move):
        # try to figure how we can bring the user move
        self.my_move = their_move
        return self.my_move

# -------------------------------------cycle player -------------------
# the cycle player will use one move as a start then cycle through them
# let's try to figure how to achieve this logic
# copy the reflect player 
class CyclePlayer(Player):
    def move(self):
        # using the self object __dict__ to check if this was the first round
        # if the __dict__ contains my_move, that means this is not the first round
        # and the learn method has been called before
        if self.__dict__.keys().__contains__("my_move"):
            if self.my_move in moves:
                index = moves.index(self.my_move)
                print(index)
                # here, we have to think of something
                # if this move index was 2, that means the we have to return the first move in the list
                if index == 2:
                    moves.append(moves[0])
                return moves[index + 1]
        else:
            return random.choice(moves)
        
    def learn(self, my_move, their_move):
        # try to figure how we can bring the user move
        self.my_move = my_move
        return self.my_move

# ---------------------------------------the game class-----------------
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
            print("That was a tie...")
            print(f"Player score is :{self.p1.score} || Random player score is: {self.p2.score}")
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
        # in this task we will calculate the final score and announce the winner.
        if self.p1.score > self.p2.score:
            print(f"The final score is player1: {self.p1.score} || player2: {self.p2.score}")
            print("Player1 wins the game")
        elif self.p1.score < self.p2.score:
            print(f"The final score is player1: {self.p1.score} || player2: {self.p2.score}")
            print("Player2 wins the game")
        else:
            print(f"The final score is player1: {self.p1.score} || player2: {self.p2.score}")
            print("No one wins the game")
        print("Game over!")


if __name__ == '__main__':
    # change this from player to human player to test 
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()

# --------------------------checking pycodestyle ------------------------
# run 
# $ pycodestyle session04.py