import random

n = int(input("Enter first number:"))
m = int(input("Enter second number:"))

list_1 = [random.randint(0, 100) for i in range(n+1)]
list_2 = [random.randint(0, 100) for i in range(m+1)]
print(f'First list: {list_1}')
print(f'Second list: {list_2}')

set_1 = set(list_1)
set_2 = set(list_2)
result = set_1.intersection(set_2)
print(f'Result: {result if len(result) > 0 else None}')