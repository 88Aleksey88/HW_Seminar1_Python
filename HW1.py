#Найдите сумму цифр трехзначного числа

a = str(input('Введите число: '))
sum = 0
i = 0
while i < len(a):
    sum = sum + int(a[i])
    i+=1
print(sum)