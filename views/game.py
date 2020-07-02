from models.board import Board
from controllers.game_rules import Game_Rules


class Game:

    def __init__(self):
        print("Let's play a game of tic tac toe!")

        self.board = Board()
        self.game_rules = Game_Rules()
        self.player_letter = "X"
        self.game_over = False

        while self.game_over != True:
            self.valid_input = False

            while self.valid_input != True:
                print(
                    f'Pick a spot from 0-8. Player letter: {self.player_letter}')
                self.player_choice = int(input())

                if self.player_choice >= 0 and self.player_choice < 9:
                    self.valid_input = True
                else:
                    print("Number not between 0 and 8!")

            self.board.the_board[int(self.player_choice)] = self.player_letter

            self.player_letter = self.game_rules.switch_player(
                self.player_letter)

            self.game_over = self.game_rules.check_for_win(
                self.board.the_board)

        print("Game Over!")
