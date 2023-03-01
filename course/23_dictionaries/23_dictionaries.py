# Name: Tommy William
# Email: memorycancel@gmail.com
# Phone: +8615666668888

customer = {
    "name": "Tommy William",
    "age": 18,
    "is_verified": True
}

customer["name"] = "Jack Dannel"
print(customer["name"])
print(customer.get("birthday")) # None
print(customer.get("birthday", "Jan 1 1999")) # default value

# exercise
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

for ch in phone:
    print(digits_mapping.get(ch, "!"))