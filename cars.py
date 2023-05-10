# Sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sort the list in reverse-alphabetical order by passing the argument reverse=True to the sort() method
cars.sort(reverse=True)
print(cars)

# Sort a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing the list in reverse order permanently, but you can reverse the orginal order by applying reverse() to the
# same list a second time
print(cars)

cars.reverse()
print(cars)

# Finding the length of a list
print(len(cars))
