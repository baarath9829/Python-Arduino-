import serial #importing serial api for serial connection
import time #importing time api for cal time
import matplotlib.pyplot as plt
sensorData = serial.Serial('com3',9600) #creating object for serial connection
xaxis = []
yaxis = []
counter = 1
while True:
    distance = []
    displacement = []
    microsec = []
    timetaken = []
    velocity = []
    retardingvelocity = []
    while True: # infinite loop
        if (sensorData.inWaiting()==0): #check for availability in serial buffer
            pass #do nothing
        else:
            distance.append(int(sensorData.readline())) # put distance cal in a list
            timer = time.time() # cal. time at which it is done  
            microsec.append(timer) # put time into a list 
            #microsec.append(float(time.time()))
        readData = raw_input('enter the brake staute \n') #check brake statues
        if(readData == '0'):break #if no brake end the loop

       # cal. difference in distance                    
    for dis in distance:
        index = distance.index(dis)
        print 'index is : ' ,index 
        if index < len(distance):
            nextdis = distance[index+1]
            dif =  dis - nextdis 
            #print dis
            print 'difference in distance',dif
            displacement.append(dif) #putting displacement into a list 

       # cal. difference in time     
    for sec in microsec:
        #print sec
        index = microsec.index(sec)
        print 'index is : ' ,index
        if index < len(microsec):
            nextvalue = microsec[index+1]
            timediff =  sec - nextvalue
            timediff = round(timediff,2)
            print 'difference is: ', abs(timediff)
            timetaken.append(timediff)# putting time difference into a list 
    print displacement
    print timetaken

    for i in range(len(displacement)):
        speed = displacement[i]/timetaken[i]
        velocity.append(speed)
        

    for vel in velocity:
        #print vel
        index = velocity.index(vel)
        print 'index is : ' ,index
        if index < len(velocity):
            nextvel = velocity[index+1]
            retardingspeed =  vel - nextvel
            print 'retarding speed is: ', retardingspeed
            retardingvelocity.append(retardingspeed)# putting retarding speed into a list

    avg_retardingvelocity = sum(retardingvelocity)/len(retardingvelocity)
    yaxis.append(avg_retardingvelocity)
    xaxis.append(counter)
    counter= counter + 1

    print 'do want to take value again or exit - 0 \n'
    data = raw_input() #check brake statues
    if(data == '0'):break #if no brake end the loop

    del distance
    del displacement
    del microsec 
    del timetaken 
    del velocity 
    del retardingvelocity      

plt.plot( xaxis ,yaxis ,'ro')
plt.plot( xaxis ,yaxis ,'b-')
plt.show()
