import math as m
import matplotlib.pyplot as plt

a = m.pi/8
print("Target value =", a)

values = []
sum_values = sum(values)
n = 0
error = []

while sum_values < 0.392:
    n += 1
    b = 1/((4 * n - 3)*(4 * n - 1))
    values.append(b)
    sum_values = sum(values)
    c = abs(a - sum_values)
    error.append(c)

x_axis = list(range(1, n+1))
print("Iteration", n, "=", sum_values)

plt.plot(x_axis, error, '.')
plt.ylabel("Absolute Error")
plt.xlabel("Iteration")
plt.show()
