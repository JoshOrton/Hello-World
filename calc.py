def multiply(x,y):
    return x*y

def subtract(x,y):
    return x-y

def divide(x,y):
    return x/y

def power(x,y):
    if (y==0):
        return 1

    elif (y<2):
         return x

    else: return x * power(x,y-1)

x = power(4,2);
print(power(4,3))
print(power(4,0))
print(x)