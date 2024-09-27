""" def area(base,height,key):
    if key == 'triangle':
        return 0.5*base*height
    elif key == 'rectangle':
        return base*height
    else:
        print("Invalid input")

print(area(12,10,'triangle')) """


def pattern(limit):
    for i in range(limit+1):
        s=''
        for j in range(i+1):
            s+='*'
        print(s)

pattern(5)