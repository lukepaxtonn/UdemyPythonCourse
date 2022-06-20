def fibonacci(n):
    """
    Fibonacci function.

    Parameters
    ----------
    n : int
        The number of iterations.

    Returns
    -------
    the `n`-th iteration of the fibonacci function, for positive `n`
    """ 
    
    if 0 <= n <= 1: 
        return n
    
    n_minus1, n_minus2 = 1,0
    result = None
    
    for f in range(n-1):
    
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    
    return result

x = input("Enter a postive integer: ")
for i in range(int(x)):
    print(i, fibonacci(i))
        