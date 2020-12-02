import joblib
import numpy as np
import xgboost
import pandas as pd
import operator
"""
0 => Human
1 => Computer
2 => Blank
"""


def dataFrameConvert(boardData: list):
    return (np.array(boardData)).reshape(1, -1)
    columns: list = [
        "ROW_1_1", "ROW_1_2", "ROW_1_3", "ROW_2_1", "ROW_2_2", "ROW_2_3",
        "ROW_3_1", "ROW_3_2", "ROW_3_3"
    ]
    board: dict = dict()
    for i in range(len(columns)):
        board[columns[i]] = [boardData[i]]
    return pd.DataFrame(data=board, columns=columns)


def NextMove(board_state: list):
    classifier = joblib.load("tic-tac-toe.joblib.dat")
    user_win = dict()
    computer_win = dict()
    print(board_state)

    if sum(board_state) == 16:
        if board_state[0] == 0:
            return 4
        elif board_state[2] == 0:
            return 4
        elif board_state[6] == 0:
            return 4
        elif board_state[8] == 0:
            return 4
        elif board_state[3] == 0:
            return 5
        elif board_state[1] == 0:
            return 7
        elif board_state[7] == 0:
            return 1
        elif board_state[5] == 0:
            return 3

    for index, element in enumerate(board_state):
        if element == 2:
            temp_state = board_state.copy()
            temp_state[index] = 0
            temp_X = dataFrameConvert(temp_state)
            score = tuple(classifier.predict_proba(temp_X))[0][1]
            user_win[index] = score

    for index, element in enumerate(board_state):
        if element == 2:
            temp_state = board_state.copy()
            temp_state[index] = 1
            print(temp_state)
            temp_X = dataFrameConvert(temp_state)
            score = tuple(classifier.predict_proba(temp_X))[0][1]
            computer_win[index] = score

    user_win_max = min(user_win.items(), key=operator.itemgetter(1))[0]
    print(computer_win)
    computer_win_max = max(computer_win.items(), key=operator.itemgetter(1))[0]
    print(user_win)

    temp_state = board_state.copy()
    temp_state[computer_win_max] = 1

    if GameStatus(temp_state)['Winner'] == 1:
        return computer_win_max

    if user_win.get(user_win_max) <= 0.5:
        return user_win_max
    else:
        return computer_win_max


def GameStatus(board_state: list):
    status = {'Winner': None, 'Cells': None}

    if (board_state[0] == board_state[1] ==
            board_state[2]) and (board_state[0] == 0 or board_state[0] == 1):
        status['Winner'] = board_state[1]
        status['Cells'] = [0, 1, 2]
    elif (board_state[3] == board_state[4] ==
          board_state[5]) and (board_state[3] == 0 or board_state[3] == 1):
        status['Winner'] = board_state[4]
        status['Cells'] = [3, 4, 5]
    elif (board_state[6] == board_state[7] ==
          board_state[8]) and (board_state[6] == 0 or board_state[6] == 1):
        status['Winner'] = board_state[7]
        status['Cells'] = [6, 7, 8]
    elif (board_state[0] == board_state[3] ==
          board_state[6]) and (board_state[0] == 0 or board_state[0] == 1):
        status['Winner'] = board_state[3]
        status['Cells'] = [0, 3, 6]
    elif (board_state[1] == board_state[4] ==
          board_state[7]) and (board_state[1] == 0 or board_state[1] == 1):
        status['Winner'] = board_state[4]
        status['Cells'] = [1, 4, 7]
    elif (board_state[2] == board_state[5] ==
          board_state[8]) and (board_state[2] == 0 or board_state[2] == 1):
        status['Winner'] = board_state[5]
        status['Cells'] = [2, 5, 8]
    elif (board_state[0] == board_state[4] ==
          board_state[8]) and (board_state[0] == 0 or board_state[0] == 1):
        status['Winner'] = board_state[4]
        status['Cells'] = [0, 4, 8]
    elif (board_state[2] == board_state[4] ==
          board_state[6]) and (board_state[2] == 0 or board_state[2] == 1):
        status['Winner'] = board_state[4]
        status['Cells'] = [0, 4, 6]

    return status


if __name__ == '__main__':
    print("Hello World")