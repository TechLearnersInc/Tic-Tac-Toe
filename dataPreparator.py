import numpy as np


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


def dataFrameDummyVar(boardData: list):
    columns: list = [
        'ROW_1_1_0', 'ROW_1_1_1', 'ROW_1_1_2', 'ROW_1_2_0', 'ROW_1_2_1',
        'ROW_1_2_2', 'ROW_1_3_0', 'ROW_1_3_1', 'ROW_1_3_2', 'ROW_2_1_0',
        'ROW_2_1_1', 'ROW_2_1_2', 'ROW_2_2_0', 'ROW_2_2_1', 'ROW_2_2_2',
        'ROW_2_3_0', 'ROW_2_3_1', 'ROW_2_3_2', 'ROW_3_1_0', 'ROW_3_1_1',
        'ROW_3_1_2', 'ROW_3_2_0', 'ROW_3_2_1', 'ROW_3_2_2', 'ROW_3_3_0',
        'ROW_3_3_1', 'ROW_3_3_2'
    ]
    pass