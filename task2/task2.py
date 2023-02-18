# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 



print("Enter a three-digit number:")
n = int(input())

sum = (n % 10) + ((n // 10) % 10) + (n // 100)

print(f"The sum of the digits is {sum}")
