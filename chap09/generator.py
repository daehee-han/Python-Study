def YourRang(start, end):
    current = start
    while current < end:
        yield current
        current += 1
    return

for i in YourRang(0, 5):
    print(i)