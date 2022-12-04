import string
from csv import reader

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priorities = {x: y for x, y in zip(letters, range(1, 53))}
# print(priorities)

# PART I
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items in the first compartment, while
# the second half of the characters represent items in the second compartment.
# with open("day_3_input.csv") as csv_file:
#     total = 0
#     for row in reader(csv_file):
#         items = row[0]
#         first, second = set(items[: len(items) // 2]), set(items[len(items) // 2 :])
#         item = first.intersection(second)
#         priority = priorities[item.pop()]
#         total += priority

#     print(total)

# PART II
with open("day_3_input.csv") as csv_file:
    total = 0
    j = 0
    lines = list(reader(csv_file))

    for i in range(3, len(lines) + 1, 3):
        group = lines[j:i]

        one = set(list(group[0][0]))
        two = set(list(group[1][0]))
        three = set(list(group[2][0]))

        badge = (one & two & three).pop()
        priority = priorities[badge]

        j = i
        total += priority

    print(total)
