# List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])  # trek
print(bicycles[0].title())  # Trek
print(bicycles[1])  # cannondale
print(bicycles[3])  # specialized
print(bicycles[-1])  # specialized, -1 return the last item in the list while -2 the second to las and so forth

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

print("-----")

# Try It Yourself

# Names - Store some names in a list called names and print each of them by accessing each element
names = ['mario', 'alexis', 'maverick']
print(names[0])
print(names[1])
print(names[2])

# Greetings - using previous list, print a message using each element
print(f"Hello, {names[0].title()}")
print(f"Hello, {names[1].title()}")
print(f"Hello, {names[2].title()}")
