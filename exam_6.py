anastasiia_birthday = "09/08/2006"

# we need to split the string into parts, otherwise it will not know what is the day, year, etc
# we convert year to integer, because otherwise it is a string
# then to consider all the years i have lived, we need to now - birth - 1
# finally converting years into days

def days_since(birthday):
    split = birthday.split("/")
    birth = int(split[2])
    now = 2026
    all = now - birth - 1
    return all * 365

print(days_since(anastasiia_birthday))