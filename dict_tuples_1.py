dict={
    'info': [500,600,700],
    'ril': [1223,431,987],
    'mtl': [232,43,123]
}


print(dict['info'][1])
def printc():
    print("hi")
    for key,values in dict.items():
        print("hi")
        print(f"{key}==> {values}==> avg: ",avg(values))

def avg(values):
    sum=0
    for i in values:
        #print(type(i))
        sum+=i
    return sum/(len(values))

def add(in2,in4):
    if in2 in dict:
        print("Stock already there ")
    else:
        dict[in2]=in4

in1=input("Please tell the operation :")
if (in1 == 'print'):
    printc()
elif (in1 == 'add'):
    in2=input("Please tell the stock you want to add")
    in3=input("please enter the price/prices with spaces ")
    in4=in3.split()
    in5=[int(i) for i in in4]
    add(in2,in5)
    printc()

else:
    print("Hi")