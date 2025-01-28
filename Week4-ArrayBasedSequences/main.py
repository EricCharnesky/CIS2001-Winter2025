import sys
from ArrayBasedSequence import ArrayBasedSequence

numbers = [ ]

print(f'size of numbers: {sys.getsizeof(numbers)}')

for number in range(1, 1000):
    numbers.append(number)
    print(f'{number}: size of numbers: {sys.getsizeof(numbers)}')



sequence = ArrayBasedSequence()


for number in range(100):
    sequence.append(number)
    print(f'{number}: size of sequence: {sys.getsizeof(sequence._data)}')


sequence[10] = 100

for index in range(len(sequence)):
    print(sequence[index])

