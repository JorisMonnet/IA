final_values = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]


def search(init):
    frontiere = [init]
    history = []
    i = 1
    while frontiere:
        print("\riteration count : {}, frontiere number :{}".format(i, len(frontiere)), end="")
        etat = frontiere.pop(0)
        history.append(etat)
        if etat.final(final_values):
            return etat
        ops = etat.applicable_operators()
        for op in ops:
            new = etat.apply(op)
            if (new not in frontiere) and new not in history and new.legal():
                #breadth first : Place children last, explore all children of depth D before going to D+1
                frontiere.append(new)
                #depth first :
                #frontiere.insert(0, new)
        i += 1

    return "No solution"