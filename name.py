name = "ada lovelace"
print(name.title())  # title() method changes each word to title case
# The dot(.) after name in name.title() tells Python to make the title() method act on the variable name
print(name.upper())  # upper() method changes each word to upper case
print(name.lower())  # lower() method changes each word to lower case

# The lower() method is useful for storing data.

print("-----")

# Using variables in strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}")

message = f"Hello, {full_name.title()}"
print(message)

print("-----")

# Adding whitespace to strings with tabs or newlines

print("Python")

print("\tPython")  # \t will add a tab to your text

print("Languages:\nPython\nC\nJavaScript")  # \n will add a newline in a string

print("Languages:\n\tPython\n\tC\n\tJavaScript")  # can combine tabs and newlines in a single string

# Stripping Whitespace

favorite_language = '     python   '
print(favorite_language)
print(favorite_language.rstrip())  # rstrip() will strip all white space to the right of the last word
print(favorite_language.lstrip())  # lstrip() will remove all white space to the left of the first word
favorite_language = '     Python is cool '
print(favorite_language.strip())
# strip() will remove all white space to the left of the first word and right of the last word
# rstrip(), lstrip() and strip() only temporarily removes the whitespace, in order to permanently remove it you must
# assign the value to the variable

# Removing Prefixes

noStarch_url = 'https://nostarch.com'
print(noStarch_url)
# Similar to the methods for removing whitespace, removeprefix() leaves the original string unchanged.  If you want to
# keep the new value, you must reassign it to the original variable or assign it to a new variable
simple_url = noStarch_url.removeprefix('https://')
print(simple_url)
