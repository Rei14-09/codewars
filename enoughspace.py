def enough(cap, on, wait):
    po = 0
    po = on+wait-cap
    if po < 1:
        return 0
    else:
        return po