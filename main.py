# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 22:36:17 2021

@author: MEDHA MATHUR
"""
class Parking:
    def __init__(self,val=0):
        self.numLots=val
        self.lots=[0]*self.numLots
    
    def park(self,rno,age):
        for l in range(len(self.lots)):
            if self.lots[l]==0:
                self.lots[l]=[rno,age]
                return l+1
        return -1           
    
    def getSlotAge(self,age):
        ans=""
        for i in range(len(self.lots)):
            if self.lots[i]==0: continue
            elif self.lots[i][1]==age:
                ans+=','+str(i+1) if len(ans)>0 else str(i+1)
        return ans
    
    def getSlotRno(self,rno):
        ans=""
        for i in range(len(self.lots)):
            if self.lots[i]==0: continue
            elif self.lots[i][0]==rno:
                ans+=','+str(i+1) if len(ans)>0 else str(i+1)
        return ans
    
    def getRno(self,age):
        ans=""
        for i in range(len(self.lots)):
            if self.lots[i]==0: continue
            elif self.lots[i][1]==age:
                ans+=','+self.lots[i][0] if len(ans)>0 else self.lots[i][0]
        return ans
    
    def leave(self,slot):
        if slot>len(self.lots):
            return 2
        elif self.lots[slot-1]==0:
            return 1
        else:
            rno,age=self.lots[slot-1][0],self.lots[slot-1][1]
            self.lots[slot-1]=0
            return [rno,age]

if __name__=="__main__":
    obj=Parking()
    file1 = open('input.txt', 'r')
    flines = file1.readlines()
    file2 = open('output.txt', 'x')
    for line in flines:
        line=line.strip()
        if line=='': break
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
            file2.write("Invalid Command\n")
    file1.close()
    file2.close()
    lines = open('output.txt', 'r').readlines() 
    del lines[-1] 
    open('output.txt', 'w').writelines(lines) 
    