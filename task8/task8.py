# Задача 8: Требуется определить, можно ли от 
# шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no


n = int(input("Enter chololate's length: "))
m = int(input("Enter chololate's width: "))
k = int(input("How many pieces do you want to break off? "))

if (k % n == 0) or (k % m == 0):
    print("yes")
else:
    print("no")