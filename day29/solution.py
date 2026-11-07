RANK = {"Must": 0, "Should": 1, "Could": 2, "Wont": 3}

def moscow_bucket(item):
    # TODO: "Must" if item["must"] is truthy; else by value/effort ratio:
    # >=3 "Should", >=1.5 "Could", else "Wont".
    pass

def prioritise(items):
    # TODO: ids sorted by (bucket rank, value/effort desc, id).
    pass

def fit_capacity(items, capacity):
    # TODO: greedily pick ids in priority order while cumulative
    # effort stays <= capacity. Return the chosen ids in order.
    pass
