import webbrowser
import time
import random
current_time = time.ctime() 
print ("start time = " + current_time)
ar=[]
for i in range(10):
    
    ar.append(i)
    
    print str(i) +" Enter Bathroom:",
    print ar
    time.sleep(random.randint(1,5))
    
    
    if i > 5:
        url="https://m.popkey.co/763f42/zaeyD.gif"
        webbrowser.open(url)
