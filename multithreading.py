import time
import threading 

def cal_square(arr):
    res=[]
    for i in arr:
        time.sleep(0.2)
        res.append(i*i)
    print(res)

def cal_cube(arr):
    res=[]
    for i in arr:
        time.sleep(0.2)
        res.append(i*i*i)
    print(res)

arr=[2,3,4]
t=time.time()
t1=threading.Thread(target=cal_square,args=(arr,))
t2=threading.Thread(target=cal_cube,args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()

print("done in: ",time.time()-t)
