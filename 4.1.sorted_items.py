items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six')]
sorted_items = sorted(items, key=lambda x: sorted_items.index(x))
print(sorted_items)
