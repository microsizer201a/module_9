def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result % 2 != 0 and result % 3 != 0:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result

result = sum_three(2, 3, 6)
print(result)