import array as arr
import random
import matplotlib.pyplot as plt
import numpy as np
import math


def run_simulation(batches, batch_size):
    global total_payout, max_payout, batch_payout, max_payout_b, batch_payouts, max_payout_bs, good_batches
    batch_payouts = arr.array('d', [])
    max_payout_bs = arr.array('d', [])
    for i in range(batches):
        batch_payout = 0
        max_payout_b = 0
        for j in range(batch_size):
            run_game()
        total_payout = total_payout + batch_payout
        batch_payouts.append(batch_payout)
        if (abs(math.log2(batch_size) / 2 - batch_payout/batch_size)) <= 0.5*math.log2(batch_size):
            good_batches = good_batches + 1
        max_payout_bs.append(max_payout_b)
        if max_payout_b > max_payout:
            max_payout = max_payout_b
    make_plots(batch_payouts)
    print("Good batch percentage:", good_batches*100/batches)
    return


def make_plots(batch_payouts):
    avg_batch_payouts = np.divide(batch_payouts, batch_size)
    plt.plot(np.arange(batches), avg_batch_payouts)
    plt.ylabel('average payout per game ($)')
    estimate = math.log2(batch_size) / 2 + math.log2(math.log2(batch_size))/2
    plt.axhline(estimate)
    plt.show()
    return


def run_game():
    global games_played, batch_payout, max_payout_b
    heads = 0
    tails = False
    while tails is False:
        flip = random.uniform(0, 1)
        if flip > 0.5:
            games_played = games_played + 1
            batch_payout = batch_payout + 2 ** heads
            if 2 ** heads > max_payout_b:
                max_payout_b = 2 ** heads
            break
        else:
            heads = heads + 1
    return


if __name__ == "__main__":
    batches = int(input('How many batches?'))
    batch_size = int(input('How many games per batch?'))
    good_batches = 0
    games_played = 0
    total_payout = 0
    max_payout = 0
    run_simulation(batches, batch_size)
    print(total_payout/(batch_size*batches), math.log2(batch_size)/2)













