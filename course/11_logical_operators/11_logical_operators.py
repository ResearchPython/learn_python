# if applicant has high income AND good credit
#     Eligible for loan

has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

# AND: both
# OR: at least one
# NOT

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "Tommy William"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")
