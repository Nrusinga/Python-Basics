dict={
    "India": 136,
    "China": 142,
    "USA": 51,
    "Pakistan": 21
}
def printc():
    for key,values in dict.items():
        print(f"{key}==>{values}")

def add(in2,in3):

    if in2 in dict:
        print("Country is already present")
    else:
        dict[in2]=in3
    
def remove(in4):
    if in4 in dict:
        del dict[in4]
    else:
        print("Country not found")

def query(in5):
    if in5 in dict:
        for key,values in dict.items():
            if in5 == key:
                print("Query found")
                print(f"{key}:{values}")
    else:
        print("query not found")

in1=input("Which operation you want to perform: ")
if (in1 == 'print'):
    printc()
elif(in1 == 'add'):
    in2=input("Which country want to add: ")
    in3=input(f"Enter the population of the country {in2}")
    add(in2,in3)
    printc()
elif(in1 == 'remove'):
    in4=input("Please enter the country you want to remove ")
    remove(in4)
    printc()
else:
    in5=input("Please query the country ")
    query(in5)

