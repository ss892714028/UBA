import random
from datetime import timedelta, date

import numpy as np
import pandas as pd

from Config import nodes, trans_matrix, start_date, end_date


def state_change(start_state, nodes, trans_matrix):
    index_list = np.arange(0, len(nodes), 1).astype(int)
    index_state = nodes.index(start_state)
    row = trans_matrix[index_state]
    end_index = np.random.choice(index_list, p=row)
    end_state = nodes[end_index]
    return end_state


def simulate(n, trans_matrix):
    state = [nodes[0]]
    start_state = 'one'
    for i in range(n):
        start_state = state_change(start_state,nodes,trans_matrix)
        # if reached conversion, append the conversion action and return
        if start_state == nodes[-2]:
            state.append(start_state)
            return state
        # if last node, customer churned, return the result immediately
        if start_state == nodes[-1]:
            return state
        state.append(start_state)
    return state


def generate_ts(start_date, end_date, k):
    res = []
    while start_date != end_date:
        start_date += timedelta(days=1)
        res.append(start_date)
    res = sorted(random.sample(res, k=k))
    return [i.strftime('%Y-%m-%d') for i in res]


def generate(num_uid, start_date, end_date):
    res = []
    for uid in range(num_uid):
        actions = simulate(7, trans_matrix)
        num_of_actions = len(actions)
        dates = generate_ts(start_date, end_date, k=num_of_actions)
        sub_table = pd.DataFrame([[uid, actions[i], dates[i]] for i in range(num_of_actions)],
                                 columns=['UID', 'Action', 'Date'])
        res.append(sub_table)

    res = pd.concat(res)
    return res


if __name__ == "__main__":
    res = generate(num_uid=100000, start_date=start_date, end_date=end_date)
    res.to_csv('data.csv', header=False, index=False)
    print(res.shape)