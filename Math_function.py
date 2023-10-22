def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Tidak bisa dibagi dengan nol")
    return a / b
