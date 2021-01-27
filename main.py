print("Первый вариант:")
x = 10
y = 120
c = x
x = y
y = c
print("x =", x)
print("y =", y)

print("Второй вариант:")
x = 10
y = 120
x = x + y
y = x - y
x = x - y
print("x =", x)
print("y =", y)

print("Третий вариант:")
x = 10
y = 120
x, y= y, x
print("x =", x)
print("y =", y)