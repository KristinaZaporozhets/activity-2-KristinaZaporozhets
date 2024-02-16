def is_prime(n):
    """
    Check if a given number is prime using an optimized algorithm.

    Parameters:
    - n (int): The number to be checked for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """

    if n < 2:
        return False
    i = 2
    while i*i <= n:
    # if n is prime has a divisor larger than its square root, 
    # it must also have a corresponding divisor smaller than its square root.
        if n % i == 0:
            return False
        i += 1
    return True

def getPrimeNumbers(n):
    res = []
    for i in range(n+1):
        if(is_prime(i)):
            res.append(i)
    return res; 


print(getPrimeNumbers(11))
