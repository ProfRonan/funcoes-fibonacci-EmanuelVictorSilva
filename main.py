def fibonacci(n):
    if n < 0:
        raise ValueError("n tem que ser maior do que zero")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b,c = 0,1,1
        for i in range(2,n + 1):
             a,b = b, a + b
        return b      

    
