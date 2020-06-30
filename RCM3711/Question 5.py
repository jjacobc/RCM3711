values = []
sum_values = sum(values)
n = 1

while sum_values < 0.392699:
    x = 1/((4*n-3)*(4*n-1))
    values.append(x)
    sum_values = sum(values)
    print(n-1, "=", sum_values)
    n += 1
