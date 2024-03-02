def swap(x,y):
    temp = x
    x = y
    y= temp
    return (x,y)
    
    
print(swap(3,5))


def swap(x,y):
    if(x<y):
        x=x+y
        y=x-y
        x=x-y
    else:
        y=y+x
        x=y-x
        y=y-x
    return (x,y)
    
print(swap(3,5))