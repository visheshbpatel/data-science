import numpy as np
from data import runs,players


def total_runs():
    player_runs = np.sum(runs, axis=1)
    d={}

    for i in range(len(players)):
        d[players[i]]=player_runs[i]

    return d



def average_run():
    avg_run = np.mean(runs, axis=1)
    d={}

    for i in range(len(players)):
        d[players[i]]=avg_run[i]

    return d



def highest_score():

    max_runs = np.max(runs)
    row= np.where(runs == max_runs)[0][0]
    max_run_player = players[row]

    return max_runs, max_run_player



