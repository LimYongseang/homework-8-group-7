def index_power(numnbers, n):
    x = len(numnbers)
    if n >= len(numnbers) or not numnbers:
        return -1
    else:
        return numnbers[n] ** n
