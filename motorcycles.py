# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati' Will change the value of index 0 to ducati instead of honda
# print(motorcycles)

# Adding elements in a list
motorcycles.append('ducati')  # append() method will add ducati to the end of the list
print(motorcycles)

# Building list dynamically
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting elements into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list
print(motorcycles)

del motorcycles[0]  # you can remove an item from any position in a list using the del statement if you know its index
print(motorcycles)

# Removing an item using the pop() method

# The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack
# motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()  # pop() method removes the last item in a list
print(motorcycles)
print(popped_motorcycle)

last_owned = popped_motorcycle  # suzuki
print(f'The last motorcycle I owned was a {last_owned.title()}.')

# Popping items from any position in a list

# You can use pop() to remove an item from any position in a list by including the index of the item you want to remove
# in parentheses
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

# Removing an item by value

# Use the remove() method when you only know the value of the item
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# The remove() method deletes only the first occurrence of the value you specify.  If there's a possiblity the value
# appears more than once in the list, you'll need to use a loop to make sure all occurrences of the value are removed.
