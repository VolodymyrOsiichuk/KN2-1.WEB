from datetime import date

#Завдання № 1
a = 15
b = 43.88884
c = "Test tset"
d = True
print()
print("Завдання № 1. Оголошення змінних та типи даних.")
print()
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print("")

#завдання №2
a = 1
b = 5
print()
print("Завдання № 2. Операції з числами.")
print()
print(F"a = {a} b = {b}")
print("+", a + b)
print("-", a - b)
print("/", a / b)
print("*", a * b)
print(f"Абсолютне значення: abs({a}) = {abs(a)}")
print(f"Модуль: {a} % {b} = {a % b}")
print("A в 2 степені", pow(a,2))
x, y, z = 43, 11, 2
average = (x + y + z) / 3
print(f"Середнє арифметичне: {average}")

#завдання №3
print()
print("Завдання № 3. Робота з рядками.")
print()
name = "Володимир"  
age = 25  
print(f"Мене звати {name} і мені {age} років.")

#завдання №4
print()
print("Завдання № 4. Умовні конструкції (if-elif-else).")
print()
number = int(input("Введіть число: "))
if number % 2 == 0:
    print(f"{number} - парне число.")
else:
    print(f"{number} - непарне число.")
number = int(input("Введіть число для перевірки (від 10 до 50): "))
if 10 <= number <= 50:
    print(f"{number} входить в діапазон.")
else:
    print(f"{number} не входить в діапазон.")

#завдання №5
print()
print("Завдання № 5. Цикли (for, while).")
print()
print("Числа від 1 до 10:")
for i in range(1,11):
    print(i)
i = 0 
sum = 0
print()
while i<101:
    print(i)
    sum += i
    i+=1
print(f"Сума чисел від 1до 100 : {sum}")

#завдання №6
print()
print("Завдання № 6. Функції.")
print()
def sum_two_numbers(a, b):
    return a + b

def reverse_string(s):
    return s[::-1]
print(sum_two_numbers(2, 12))
print(reverse_string("Hello World"))

#завдання №7
print()
print("Завдання № 7. Списки та цикли.")
print()
str_list = ["asd","asd","bbb","ddd",'ggg']
for element in str_list:
    print(element)
print("Додано елемент до списку")
str_list.append("ggg")
print(str_list)
print("Видалено останній елемент в списку")
str_list.pop()
print(str_list)

#завдання №8
print()
print("Завдання № 8. Робота з словниками.")
print()
student = {
    "Name" : "Oleh",
    "Age" : 25,
    "Faculty" : "Computer Science"
}
print(student["Name"])
student["Year of study"] = date.today().strftime("%Y")
print(student)

#завдання №9
print()
print("Завдання № 9. Обробка виключень (try-except).")
print()
try:
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    print(f"a/b = {a/b}")
except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе.")
except:
    print("Виникла інша помилка.")
