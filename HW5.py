# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [2, 3, 4, 5, 6]
i = 0
newlist = []
if len(list)%2 == 0:
    while i < len(list)//2:
        newlist.append(list [i] * list [len(list)-1-i])
        i+=1
else:
    while i < len(list)//2 + 1:
        newlist.append(list [i] * list [len(list)-1-i])
        i+=1
print(newlist)