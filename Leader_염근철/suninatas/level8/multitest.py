from concurrent.futures import ThreadPoolExecutor




def print1():
    for i in range(10):
        print (i)
def print2():
    for i in range(10):
        print (i)
def print3():
    for i in range(10):
        print (i)
        
with ThreadPoolExecutor(max_workers=3) as executor:
    proc1=executor.submit(print1,)
    proc2=executor.submit(print2,)
    proc3=executor.submit(print3,)




