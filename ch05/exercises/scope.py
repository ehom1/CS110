# 1
def accum(x):
    count = 0
    for _ in range(x):
        count = count + x
    
    return count 

# 2 
def expo(number, exponent):
    result = number ** exponent
    return result 

#3 
def square(z):
    return accum(z)
    
print(accum(10))
print(expo(2, 3))
print(square(5))