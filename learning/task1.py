#  Знайти суму елементів, які знаходяться після першого 0

lst = [int(input('Enter element: ')) for x in range(7)]
zero_index = -100
for i in range(len(lst)):
    if lst[i] == 0:
        zero_index = i
        break
res = sum(lst[zero_index+1::])
print(res)

