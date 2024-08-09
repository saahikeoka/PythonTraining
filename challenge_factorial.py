def factorial(fac_num): 
    returned = 1
    for item in range(fac_num, 1, -1):
        returned *= item

    # while fac_num > 0:
    #     returned *= fac_num
    #     fac_num -= 1

    return returned
    
print(factorial(3))
print(factorial(4))
print(factorial(5))
