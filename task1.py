# 1.Напишите функцию которая будет суммировать
# введенные три случайные цифры.
def add():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))
    summa = number1 + number2 + number3
    return summa

print(add())