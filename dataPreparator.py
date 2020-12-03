import os
import numpy as np
import pandas as pd

os.system('cls')


def numpyConvert(boardData: list):
    return (np.array(boardData)).reshape(1, -1)


def dataFrameConvert(boardData: list):
    columns: list = [
        "ROW_1_1", "ROW_1_2", "ROW_1_3", "ROW_2_1", "ROW_2_2", "ROW_2_3",
        "ROW_3_1", "ROW_3_2", "ROW_3_3"
    ]
    board: dict = dict()
    for i in range(len(columns)):
        board[columns[i]] = [boardData[i]]
    return pd.DataFrame(data=board, columns=columns)


def dataFrameDummyVarConvert(boardData: list):
    columns: list = [
        'ROW_1_1_0', 'ROW_1_1_1', 'ROW_1_1_2', 'ROW_1_2_0', 'ROW_1_2_1',
        'ROW_1_2_2', 'ROW_1_3_0', 'ROW_1_3_1', 'ROW_1_3_2', 'ROW_2_1_0',
        'ROW_2_1_1', 'ROW_2_1_2', 'ROW_2_2_0', 'ROW_2_2_1', 'ROW_2_2_2',
        'ROW_2_3_0', 'ROW_2_3_1', 'ROW_2_3_2', 'ROW_3_1_0', 'ROW_3_1_1',
        'ROW_3_1_2', 'ROW_3_2_0', 'ROW_3_2_1', 'ROW_3_2_2', 'ROW_3_3_0',
        'ROW_3_3_1', 'ROW_3_3_2'
    ]

    board: dict = dict()
    for i in range(len(columns)):
        board[columns[i]] = [0]

    for rowNo in range(1, 4):
        for cellNo in range(1, 4):
            board[f'ROW_{rowNo}_{cellNo}_{boardData[cellNo-1]}'] = 1

    return pd.DataFrame(data=board, columns=columns)


if __name__ == '__main__':
    print('Hello World')
