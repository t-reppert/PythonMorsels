

def parse_ranges(text):
    items = text.split(',')
    for item in items:
        if '->' in item:
            first, second = item.split('->')
            yield int(first)
        elif '-' in item:
            first, second = item.split('-')
            for x in range(int(first), int(second)+1):
                yield x
        else:
            yield int(item)
