
from collections.abc import Iterable
from datetime import timedelta


def deep_add(nums, start=0):
    if start == 0:
        s = []
    else:
        s = [start]
    for i in nums:
        if isinstance(i, Iterable):
            if len(i) > 0:
                s.append(deep_add(i))
        else:
            s.append(i)
    if len(s) > 0 and type(s[0]) == timedelta:
        result = sum(s, timedelta())
    else:
        result = sum(s)
    return result

