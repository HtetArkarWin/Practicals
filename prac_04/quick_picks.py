import random

quick_picks_bets = []
no_of_quick_pick = int(input("How many quick picks? "))
for no in range(no_of_quick_pick):

    quick_picks = [0,0,0,0,0,0]
    quick_picks[0] = 0
    quick_picks[1] = 0
    quick_picks[2] = 0
    quick_picks[3] = 0
    quick_picks[4] = 0
    quick_picks[5] = 0
    random_number = random.randint(1,45)
    for i in range(0,6):
        random_number = random.randint(1,45)
        while random_number in quick_picks:
            random_number = random.randint(1, 45)
        quick_picks[i] = random_number
    quick_picks.sort()
    quick_picks_bets.append(quick_picks)
print(quick_picks_bets)

for list in quick_picks_bets:
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(list[0],list[1],list[2],list[3],list[4],list[5]))