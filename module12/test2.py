import sys
import time
start = time.time()
print start 
time.clock()
print start
elapsed = 0
seconds=3
i=0 
print i
try:
    while elapsed < seconds:
        print time.time() 
        elapsed = time.time() - start
        print 'e %s'%elapsed
        #time.sleep(1)
        i+=1
    if elapsed==seconds:
        print i
        print("time out")
except:
    pass
