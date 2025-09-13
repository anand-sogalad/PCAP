import random
import platform

# get random floating point numbe between 0 and 1
print(random.random())

# randrange
print(random.randrange(1, 100))

# randint
print(random.randint(1, 100))

# shuffle
print(random.shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# choice
print(random.choice([1, 2, 3, 4, 5]))

# sample
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

# platform
print(platform.platform())

# processor
print(platform.processor())

# machine
print(platform.machine())

# architecture
print(platform.architecture())

# python_version
print(platform.python_version())

# system
print(platform.system())

# version
print(platform.version())
