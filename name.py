name = "ada lovelace"
print(name.title())  # title() method changes each word to title case
# The dot(.) after name in name.title() tells Python to make the title() method act on the variable name
print(name.upper())  # upper() method changes each word to upper case
print(name.lower())  # lower() method changes each word to lower case

# The lower() method is useful for storing data.

print("-----")

# full_name.py

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}")

message = f"Hello, {full_name.title()}"
print(message)
