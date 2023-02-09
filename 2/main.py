import random

n = int(input("Enter number of bushes >=3 :"))
list_1 = [random.randint(1, 100) for _ in range(n)]
print(f'Quantity of berries on bushes: {list_1}')

quantity = list_1[0] + list_1[n - 1] + (list_1[n - 2] if list_1[n - 2] > list_1[1] else list_1[1])
for i in range(1, n - 1):
    curr_quantity = list_1[i - 1] + list_1[i] + list_1[i + 1]
    if curr_quantity > quantity:
        quantity = curr_quantity
print(f'Maximum quantity of berries: {quantity}')
