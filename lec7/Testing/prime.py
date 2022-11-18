def is_prime(n):
    if n < 2:
        return False
    else:
        if n % 2 != 0 or n % 3 != 0:
            return True
    return False

assert is_prime(105) == False
