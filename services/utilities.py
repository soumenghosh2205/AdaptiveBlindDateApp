import numpy as np
import pandas as pd


def euclidean_distance(arr1, arr2):
    """
    Used by recommender system to find similarity between
    1. users
    2. activity and user
    :param arr1: first array
    :param arr2: second array
    :return: Finding the euclidean distance (RMSE) between 2 arrays
    """
    d = np.linalg.norm(np.subtract(arr1,arr2))
    return d


def json_to_df(json, columns=None):
    df = pd.DataFrame(json).T
    # df.rename(columns={"index":"id"},inplace=True)
    # df = pd.DataFrame(json).T.reset_index()
    if columns is not None:
        df = df.loc[:, df.columns.str.contains('|'.join(columns))]
    return df

def calculate_similarity(data_df,ideal_df):
    score_dict ={}
    l1 = len(data_df)
    for i in range(l1):
        arr1 = ideal_df.iloc[i, :].values
        user_id_1 = ideal_df.index[i]
        score_other_list = []
        for j in range(i + 1, l1):
            arr2 = data_df.iloc[j, :].values
            score_other_list.append(euclidean_distance(arr1, arr2))
        score_dict[user_id_1] = score_other_list
    #del score_dict[user_id_1]
    return score_dict


def find_match_score(self_score, ideal_score):
    match_score = {}
    temp1, temp2 = 0, 0
    f = 1
    for key1, values1 in self_score.items():
        if (len(values1) == 0):
            continue
        temp1 = self_score[key1]
        temp2 = ideal_score[key1]
        temp_list = []
        for value1, value2 in zip(temp1, temp2):
            temp_list.append((value1 + value2) // 2)
            m = max(temp_list)
        match_score[key1] = [m, [list(self_score.keys())[x + f] for x, y in enumerate(temp_list) if y == m]]
        f = f + 1
    return match_score


def main():
    arr1 = []
    arr2 = []
    euclidean_distance(arr1, arr2)


if __name__ == '__main__':
    main()