numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.insert(0, 10)
print(numbers)

# sort() index() remove() pop() reverse()

numbers = [1, 1, 2, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)