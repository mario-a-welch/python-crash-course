# Personal Message

name = 'Mario'
print(f"Hello {name}, would you like to learn some Python today?")

# Name Cases
# Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case

print(name.lower())
print(name.upper())
print(name.title())

# Famous Quote
# Find a quote from a famous person you admire. Print the quote and the name of its author, include the quotation marks

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# Famous Quote 2
# Represent the famous person's name using a variable called famous_person.  Then compose your message and represent it
# with a new variable called message.  Print your message

famous_person = 'Albert Einstein'
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

# Stripping Names
name = '\t     Mario Welch    \n '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# File Extensions
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
