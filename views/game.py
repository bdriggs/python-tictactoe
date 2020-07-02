from models.board import Board
from controllers.game_rules import Game_Rules


class Game:

    def __init__(self):
        print("Let's play a game of tic tac toe!")

        board = Board()
        game_rules = Game_Rules()
        player_letter = "X"

        game_over = False
        while game_over != True:
            print("Pick a spot from 0-8")
            player_choice = input()

            board.the_board[int(player_choice)] = player_letter

            player_letter = game_rules.switch_player(player_letter)

            game_over = game_rules.check_for_win(board.the_board)

        print("Game Over!")
