import random

flip_coin = int(input("How many times you want to flip the coin : "))
flip_coin_range = range(flip_coin)
head = 0
tail = 0

print("Coin flipping : ",flip_coin,"times")

for coin in flip_coin_range:

    if random.randint(0, 1) == 1:
        head += 1
    else:
        tail += 1

percent_head = ((head/flip_coin) * 100)
percent_tail = ((tail / flip_coin) * 100)

print("Head Percentage : ", percent_head, "%")
print("Tail Percentage : ", percent_tail, "%")

