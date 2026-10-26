def money_change(money):

    if money.isdigit() or money < 0:
        return None

    list_coins = [5, 2, 1]
    change = []
    for coin in list_coins:
        change.append(money // coin)
        money = money % coin

    assert not money

    return tuple(change)


print(money_change(8))
# >>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(money_change(5))
# >>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(money_change(29))
# >>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(money_change(0))
# >>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
print(money_change(170))
# >>> (34, 0, 0)  # treinta y cuatro de 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(money_change(267))
# >>> (53, 1, 0)  # cincuenta y tres de 5 cénts, una de 2 cénts y ninguna de 1 cént.
print(money_change(-2))
# >>> None
print(money_change(5.576))
# >>> None
print(money_change("5"))
# >>> None
