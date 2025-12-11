"""Is even"""
def is_even(k):
    """Start"""
    if (k & 1) == 0:
        return True
    else:
        return False

number = int(input())
print(is_even(number))
