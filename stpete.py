import random
import array as arr



def run_simulation(batches, batch_size):
    global total_payout, max_payout, batch_payout, max_payout_b, batch_payouts
    batch_payouts = arr.array('d', [])
    for i in range(batches):
        batch_payout = 0
        max_payout_b = 0
        for j in range(batch_size):
            run_game()
        total_payout = total_payout + batch_payout
        batch_payouts.append(batch_payout)
        if max_payout_b > max_payout:
            max_payout = max_payout_b
    print(batch_payouts)
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


#click to run
if __name__ == "__main__":
    batches = int(input('How many batches?'))
    batch_size = int(input('How many games per batch?'))
    games_played = 0
    total_payout = 0
    max_payout = 0
    run_simulation(batches, batch_size)













