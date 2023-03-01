import random

for i in range(3):
    print(random.randint(10, 20))

for i in range(3):
    print(random.random())

members = ['John', 'Mary', 'Bob', 'Mash']
leader = random.choice(members)
print(leader)

