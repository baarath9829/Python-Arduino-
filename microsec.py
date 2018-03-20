import time
microsec = []
for i in range(10):
    timer = time.time()
    microsec.append(timer)
    print time.time()
    print timer,'timer timing'

for sec in microsec:
    print sec
    index = microsec.index(sec)
    if index <> len(microsec):
        nextvalue = microsec[index+1]
        timediff =  sec - nextvalue
        print round(timediff,2)
        print 'difference is: ', timediff
        
