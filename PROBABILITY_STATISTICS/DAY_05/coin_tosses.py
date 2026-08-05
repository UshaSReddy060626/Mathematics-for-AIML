import random
heads = 0
tails = 0
for _ in range(20):
    toss = random.choice(["H", "T"])
    if toss == "H":
        heads += 1
    else:
        tails += 1
print("Heads:", heads)
print("Tails:", tails)