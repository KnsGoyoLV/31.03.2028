# TODO: Salabo kļūdas un uzlabo šo kodu!

def greet(name):
    return f"Hello there, {name}"

def calculate_age(year_of_birth):
    year = "2025"
    return year - year_of_birth  # Kļūda: year ir str, nevis int

print(greet("Anna"))
age = calculate_age(2007)
print("You are", age, "years old")
