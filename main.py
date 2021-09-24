# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 22:36:17 2021

@author: MEDHA MATHUR
"""
class Parking:
    #Create Parking lot of given size(val)
    def __init__(self,val=0):
        self.numLots=val
        self.lots=[0]*self.numLots #Initialize to 0
    
    #Park car into nearest available lot by traversing from 1st to last lot
    def park(self,rno,age):
        for l in range(len(self.lots)):
            if self.lots[l]==0:
                self.lots[l]=[rno,age]
                return l+1
        return -1 #If no slot is available          
    
    #Get all slot numbers corresponding to given age
    def getSlotAge(self,age):
        ans=""
        for i in range(len(self.lots)):
            if self.lots[i]==0: continue #No car parked in this lot
            elif self.lots[i][1]==age:
                ans+=','+str(i+1) if len(ans)>0 else str(i+1)
        return ans #comma separated slots outputed
    
    #Get all slot numbers corresponding to given Registration Number
    def getSlotRno(self,rno):
        ans=""
        for i in range(len(self.lots)):
            if self.lots[i]==0: continue #No car parked in this lot
            elif self.lots[i][0]==rno:
                ans+=','+str(i+1) if len(ans)>0 else str(i+1)
        return ans #comma separated slots outputed
    
    #Get all Registration Numbers corresponding to given age
    def getRno(self,age):
        ans=""
        for i in range(len(self.lots)):
            if self.lots[i]==0: continue #No car parked in this lot
            elif self.lots[i][1]==age:
                ans+=','+self.lots[i][0] if len(ans)>0 else self.lots[i][0]
        return ans #comma separated Registration Numbers outputed
    
    #Vacate the given slot
    def leave(self,slot):
        # If input slot number is more than size of parking lot
        if slot>len(self.lots):
            return 2
        elif self.lots[slot-1]==0:
            return 1 #The input slot is already empty
        else:
            rno,age=self.lots[slot-1][0],self.lots[slot-1][1]
            self.lots[slot-1]=0
            return [rno,age] # Returning details of driver who vacated slot

if __name__=="__main__":
    obj=Parking() #Create an empty object
    #opening input and output files 
    file1 = open('input.txt', 'r') 
    flines = file1.readlines() 
    file2 = open('output.txt', 'x')
    for line in flines:
        line=line.strip()
        if line=='': break #If EOF is reached, we stop processing
        #Splitting the command name from the inputs
        cmd = list(map(str,line.split()))
        if cmd[0]=="Create_parking_lot":
            obj=Parking(int(cmd[1]))
            file2.write("Created parking of {} slots".format(int(cmd[1]))+'\n')
        elif cmd[0]=="Park":
            slot=obj.park(cmd[1], int(cmd[3]))
            if slot==-1:
                file2.write("The Parking lot is full\n")
            else:
                file2.write("Car with vehicle registration number \"{}\" has been parked at slot number {}\n".format(cmd[1],slot))
        elif cmd[0]=="Slot_numbers_for_driver_of_age":
            ans=obj.getSlotAge(int(cmd[1]))
            file2.write(ans+'\n')
        elif cmd[0]=="Slot_number_for_car_with_number":
            ans=obj.getSlotRno(cmd[1])
            file2.write(ans+'\n')
        elif cmd[0]=="Leave":
            ans=obj.leave(int(cmd[1]))
            if ans==2:
                file2.write("Slot does not exist in Parking Lot\n")
            elif ans==1:
                file2.write("Slot already vacant\n")
            else:
                file2.write("Slot number {} vacated, the car with vehicle registration number \"{}\" left the space, the driver of the car was of age {}\n".format(int(cmd[1]),ans[0],ans[1]))
        elif cmd[0]=="Vehicle_registration_number_for_driver_of_age":
            ans=obj.getRno(cmd[1])
            file2.write(ans+'\n')
        else:
            file2.write("Invalid Command\n") #If any other command is entered, then it is INVALID
    file1.close()
    file2.close()
    #Removing the last line from output file which is an extra '\n'
    """lines = open('output.txt', 'r').readlines() 
    del lines[-1] 
    open('output.txt', 'w').writelines(lines) 
    """