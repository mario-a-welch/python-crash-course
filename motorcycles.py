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
