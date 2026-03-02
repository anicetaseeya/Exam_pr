import random

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(1, 100))

# len(random_numbers) returns number of elements in list, important when modifying
# lists are mutable
# we use elif (we could have used just if) because numbers cannot be both more than 80 and less than 40
# we need random_numbers[i] = s so it actually replaces the old number in the list with the new value

for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]
    elif random_numbers[i] < 40:
        num = random_numbers[i]
        s = 0
        while num > 0:
            s += num % 10
            num = num // 10
        random_numbers[i] = s

print(random_numbers)