def fibonacci(n):

    if (n == 0):
        return []
    if (n == 1):
        return [1]

    fibonacci = [0] * (n)
    fibonacci[0] = 1
    fibonacci[1] = 1
    for i in range(2,n):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]


    return fibonacci

# Exemple de test:


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(7))
print(fibonacci(10))
print(fibonacci(20))
print(fibonacci(30))



