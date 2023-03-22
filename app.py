import random

from flask import Flask, render_template

import numtocords

app = Flask(__name__)


def checkwinner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return (str(board[i][0]) + " is winner")
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return (str(board[0][i]) + " is winner")
    if board[0][0] == board[1][1] == board[2][2]:
        return (str(board[0][0]) + " is winner")
    elif board[0][2] == board[1][1] == board[2][0]:
        return (str(board[1][1]) + " is winner")
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                return 0
    return 'draw'


def get_computer_move(board):
    # Defeat the user
    for i in range(3):
        if board[i][0] == board[i][1] == 'O' and type(board[i][2]) == int:
            return (i, 2)

    for i in range(3):
        if board[i][0] == board[i][2] == 'O' and type(board[i][1]) == int:
            return (i, 1)

    for i in range(3):
        if board[i][1] == board[i][2] == 'O' and type(board[i][0]) == int:
            return (i, 0)

    for i in range(3):
        if board[0][i] == board[1][i] == 'O' and type(board[2][i]) == int:
            return (2, i)

    for i in range(3):
        if board[0][i] == board[2][i] == 'O' and type(board[1][i]) == int:
            return (1, i)
    for i in range(3):
        if board[1][i] == board[2][i] == 'O' and type(board[0][i]) == int:
            return (0, i)

    if board[0][0] == board[1][1] == 'O' and type(board[2][2]) == int:
        return (2, 2)
    elif board[0][0] == board[2][2] == 'O' and type(board[1][1]) == int:
        return (1, 1)
    elif board[1][1] == board[2][2] == 'O' and type(board[0][0]) == int:
        return (0, 0)
    elif board[0][2] == board[1][1] == 'O' and type(board[2][0]) == int:
        return (2, 0)
    elif board[0][2] == board[2][0] == 'O' and type(board[1][1]) == int:
        return (1, 1)
    elif board[2][0] == board[1][1] == 'O' and type(board[0][2]) == int:
        return (0, 2)

    # blocking the user
    for i in range(3):
        if board[i][0] == board[i][1] == 'X' and type(board[i][2]) == int:
            return (i, 2)

    for i in range(3):
        if board[i][0] == board[i][2] == 'X' and type(board[i][1]) == int:
            return (i, 1)

    for i in range(3):
        if board[i][1] == board[i][2] == 'X' and type(board[i][0]) == int:
            return (i, 0)

    for i in range(3):
        if board[0][i] == board[1][i] == 'X' and type(board[2][i]) == int:
            return (2, i)

    for i in range(3):
        if board[0][i] == board[2][i] == 'X' and type(board[1][i]) == int:
            return (1, i)
    for i in range(3):
        if board[1][i] == board[2][i] == 'X' and type(board[0][i]) == int:
            return (0, i)

    if board[0][0] == board[1][1] == 'X' and type(board[2][2]) == int:
        return (2, 2)
    elif board[0][0] == board[2][2] == 'X' and type(board[1][1]) == int:
        return (1, 1)
    elif board[1][1] == board[2][2] == 'X' and type(board[0][0]) == int:
        return (0, 0)
    elif board[0][2] == board[1][1] == 'X' and type(board[2][0]) == int:
        return (2, 0)
    elif board[0][2] == board[2][0] == 'X' and type(board[1][1]) == int:
        return (1, 1)
    elif board[2][0] == board[1][1] == 'X' and type(board[0][2]) == int:
        return (0, 2)

    # Check for center space
    if type(board[1][1]) == int:
        return (1, 1)

    # Check for corners
    if type(board[0][0]) == int:
        return (0, 0)
    if type(board[0][2]) == int:
        return (0, 2)
    if type(board[2][0]) == int:
        return (2, 0)
    if type(board[2][2]) == int:
        return (2, 2)

    # Check for edges
    if type(board[0][1]) == int:
        return (0, 1)
    if type(board[1][0]) == int:
        return (1, 0)
    if type(board[1][2]) == int:
        return (1, 2)
    if type(board[2][1]) == int:
        return (2, 1)


board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]




@app.route('/')
def home():
    for i in range(1, 10):
        j, k = numtocords.num_to_coords(i)[0], numtocords.num_to_coords(i)[1]
        board[j][k] = i
    players = ['X', 'O']
    trn = random.sample(players, 1)[0]
    print(trn)
    if trn == 'O':
        j, k = get_computer_move(board)[0], get_computer_move(board)[1]
        board[j][k] = 'O'
    return render_template('index.html', board=board)


@app.route('/button_clicked/<int:button_number>')
def button_clicked(button_number):
    message = "You clicked button {}!".format(button_number)
    return message

@app.route('/choice')
def choice():
    return render_template('playerchoice.html')

@app.route("/play/<int:move>")
def play(move):
    text = ''
    if not checkwinner(board):
        j, k = numtocords.num_to_coords(move)[0], numtocords.num_to_coords(move)[1]
        if type(board[j][k]) == int:
            board[j][k] = 'X'
            if not checkwinner(board):
                j, k = get_computer_move(board)[0], get_computer_move(board)[1]
                board[j][k] = 'O'
                if checkwinner(board):
                    text = checkwinner(board)
                    return render_template('index.html', board=board, text=text)
            else:
                text = checkwinner(board)
            return render_template('index.html', board=board, text=text)
    else:
        text = checkwinner(board)
        return render_template('index.html', board=board, text=text)






if __name__ == '__main__':
    app.run(debug=True)
