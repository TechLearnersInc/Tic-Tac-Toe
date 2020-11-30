import joblib
import numpy as np
import xgboost
import pandas as pd


def data_frame_convert(boardData):
    columns: tuple = ("ROW_1_1", "ROW_1_2", "ROW_1_3", "ROW_2_1", "ROW_2_2",
                      "ROW_2_3", "ROW_3_1", "ROW_3_2", "ROW_3_3")
    board: dict = dict()
    for i in range(len(columns)):
        board[columns[i]] = [boardData[i]]
    return pd.DataFrame(data=board, columns=columns)


def main():
    board_state = [0, 2, 1, 2, 0, 2, 2, 2, 2]
    classifier = joblib.load("tic-tac-toe.joblib.dat")
    user_win = dict()
    computer_win = dict()
    for index, element in enumerate(board_state):
        if element == 2:
            temp_state = board_state.copy()
            temp_state[index] = 0
            temp_X = data_frame_convert(temp_state)
            score = 1 - (classifier.predict_proba(temp_X))[0][1]
            user_win[index] = score

    for index, element in enumerate(board_state):
        if element == 2:
            temp_state = board_state.copy()
            temp_state[index] = 1
            temp_X = data_frame_convert(temp_state)
            score = tuple(classifier.predict_proba(temp_X))[0][1]
            computer_win[index] = score

    user_win_max = user_win.get(max(user_win))
    print(user_win_max)
    computer_win_max = computer_win.get(max(computer_win))
    print(computer_win_max)

    if user_win_max > computer_win_max:
        return max(user_win)
    else:
        return max(computer_win)


if __name__ == '__main__':
    print(main())