
def uniques_only(nums):
    hashable = set()
    unhashable = []
    for n in nums:
        try:
            if n not in hashable:
                yield n
                hashable.add(n)
        except TypeError:
            if n not in unhashable:
                yield n
                unhashable.append(n)





