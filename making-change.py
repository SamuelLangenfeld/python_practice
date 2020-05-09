# Given a list of possible coins in cents, and an amount (in cents) n,
# return the minimum number of coins needed to create the amount n.
# If it is not possible to create the amount using the given coin denomination,
# return None.

# Here's an example and some starter code:


def make_change(coins, n):
     # naive approach -> subtract large coins until the amount is too low, go down 
     # to next denomination
    coins.sort()
    coins.reverse()
    current_amount = n
    coins_used = []
    for coin in coins:
        while current_amount >= coin:
            current_amount = current_amount - coin
            coins_used.append(coin)
    if current_amount > 0:
        return None
    return coins_used

print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
