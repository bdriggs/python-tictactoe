import os
os.sys.path.append("/home/briggs/Documents/repos/python-tictactoe")
from models.board import Board

class Game_Rules:
    def __init__(self):
        self.game_over = False

    def switch_player(self, player_letter):
        if player_letter == "X":
            player_letter = "O"
            return player_letter
        elif player_letter == "O":
            player_letter = "X"
            return player_letter

    def check_for_win(self, board):
        if board[0] == "X" and board[1] == "X" and board[2] == "X":
            self.game_over = True
            return self.game_over
        elif board[3] == "X" and board[4] == "X" and board[5] == "X":
            self.game_over = True
            return self.game_over
        elif board[6] == "X" and board[7] == "X" and board[8] == "X":
            self.game_over = True
            return self.game_over
        elif board[0] == "X" and board[4] == "X" and board[8] == "X":
            self.game_over = True
            return self.game_over
        elif board[2] == "X" and board[4] == "X" and board[8] == "X":
            self.game_over = True
            return self.game_over
        elif board[0] == "O" and board[1] == "O" and board[2] == "O":
            self.game_over = True
            return self.game_over
        elif board[3] == "O" and board[4] == "O" and board[5] == "O":
            self.game_over = True
            return self.game_over
        elif board[6] == "O" and board[7] == "O" and board[8] == "O":
            self.game_over = True
            return self.game_over
        elif board[0] == "O" and board[4] == "O" and board[8] == "O":
            self.game_over = True
            return self.game_over
        elif board[2] == "O" and board[4] == "O" and board[8] == "O":
            self.game_over = True
            return self.game_over
        else: return self.game_over
        
        
    
