'''
function iterativePower
    result=1
    for exponent value 
    result = result*base 
    return result
print result

'''
def iterativePower (base,exp):
    result = 1

    for i in range(exp):
        result *= base
    return result

print(iterativePower(5,3))


#-------------------------------------------------------------------------------------------------

'''
function recursivePower
    if exp=1
    return the base
    else
    return base*return from exp - 1
print result

'''
base = 0
exp = 0

def recursivePower (base,exp):

    if exp == 1:
        return base
    else:
        return base * (recursivePower(base, exp - 1))


print(recursivePower(12,2))
