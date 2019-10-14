from collections import deque


def tail(items, n):
    if n <= 0:
        return []
    new_items = deque(maxlen=n)
    for i in items:
        new_items.append(i)
    return list(new_items)

