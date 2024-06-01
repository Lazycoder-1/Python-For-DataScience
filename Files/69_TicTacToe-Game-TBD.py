# the tictactoe game
import random

board = [" "] * 9
def draw_board(board):
    row_1 = "{}|{}|{}".format(board[0], board[1], board[2])
    row_2 = "{}|{}|{}".format(board[3], board[4], board[5])
    row_3 = "{}|{}|{}".format(board[6], board[7], board[8])

while 1 == 1:
    user_input = int(input('Choose number between 1 and 9: '))
    user_input =- 1
    board[user_input] = 'x'
    draw_board(board)


print(row_1+'\n'+ row_2 + '\n' + row_3)