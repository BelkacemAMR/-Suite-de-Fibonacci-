if (n == 0):
    return []
if (n == 1):
    return [1]

fibonacci = [0] * (n)
fibonacci[0] = 1
fibonacci[1] = 1
for i in range(2, n):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

return fibonacci