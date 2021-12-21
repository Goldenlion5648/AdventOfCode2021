import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input21.txt")
inp = a.data

board = list(range(1, 11))
def play(start1, start2):
    pos1 = start1 - 1
    pos2 = start2 - 1
    score1 = 0
    score2 = 0
    num = 1
    rolls = 0
    for i in range(10000):
        for j in range(1, 4):
            if i % 2== 0:
                pos1 += num
            else:
                pos2 += num
            rolls += 1
            num += 1
            if num == 101:
                num = 1
        if i % 2 == 0:
            score1 += board[pos1 % len(board)]
        else:
            score2 += board[pos2 % len(board)]
        if score1 >= 1000:
            return (score2 * rolls)
        if score2 >= 1000:
            return (score1 * rolls)


ways_to_get_dice_total = Counter()
for x in distinct_permutations([1, 2, 3]*3, 3):
    ways_to_get_dice_total[sum(x)] += 1

printd(ways_to_get_dice_total)
def play_quantum(start):
    # turn number -> score -> positions : ways_to_get_to
    dp = dd(lambda : dd(lambda : Counter()))
    dp[1][0][start] = 1
    # turn num to score to ways_score_was_achieved
    turn_num_states = dd(lambda : Counter())
    for i in range(1, 25):
        for score in dp[i]:
            if score >= 21:
                continue
            for prev_pos, times_seen in dp[i][score].items():
                for roll_num, ways_to_get in (ways_to_get_dice_total.items()):
                    new_pos = prev_pos + roll_num
                    if new_pos > 10:
                        new_pos %= 10
                    new_score = score+(new_pos)
                    dp[i+1][new_score][new_pos] += times_seen * ways_to_get
                    turn_num_states[i][new_score] += (times_seen * ways_to_get)

    return turn_num_states

def part2(pos1, pos2):
    player1 = play_quantum(pos1)
    player2 = play_quantum(pos2)

    total_wins = Counter()
    for turn_num in range(3, 15):
        for winning_score in range(21, 31):
            total_wins[1] += player1[turn_num][winning_score] * sum(player2[turn_num-1][j] for j in range(1, 21)) 
            total_wins[2] += player2[turn_num][winning_score] * sum(player1[turn_num][j] for j in range(1, 21)) 
    return max(total_wins[1], total_wins[2])

assert play(4, 8) == 739785
ans(play(3, 5))
assert part2(4, 8) == 444356092776315
ans(part2(3, 5))
