from itertools import groupby


def compact(values):
    if not values:
        return []
    for k, g in groupby(values):
        yield k



