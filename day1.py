from csv import reader

# PART I
# Find out which elf is carrying the most calories
def total_elf_calories_descending():
    with open("day_1_input.csv", "r") as csv_file:
        elf_calories = []
        calorie_count = 0
        csv_reader = reader(csv_file)

        for row in csv_reader:
            if row:
                calories = int(row[0])
                calorie_count += calories
            else:
                elf_calories.append(calorie_count)
                calorie_count = 0

        elf_calories.sort(reverse=True)
        # print("This is elf_calories: ", elf_calories)

        return elf_calories


# PART II
# Get the total calories carried by the top 3 elves
elf_calories_list = total_elf_calories_descending()
total = elf_calories_list[0] + elf_calories_list[1] + elf_calories_list[2]
print(total)
