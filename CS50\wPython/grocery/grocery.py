groceries = {}
while True:
    try:
        item = input("").lower().strip()
    except EOFError:
        break
    if item.upper() in groceries:
        groceries[item.upper()] += 1
    else:
        groceries[item.upper()] = 1

sorted_items = sorted(groceries.items())
sorted_groceries = dict(sorted_items)

for thing in sorted_groceries:
    print(f"{groceries[thing]} {thing}")