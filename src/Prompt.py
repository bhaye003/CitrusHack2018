import midi
import random

class Prompt:
    def Options(self, bars, isVel, vel, scale, tempo):
        userBars = ""
        #default = 1
        velDefault = ""
        userVel = ""
        #default = 100
        velVal = 0
        userSca = ""
        userTemp = ""
        print("Enter the number of bars/measures, or choose to retain default settings. (Enter as an integer value or enter 'default')")
        userBars = input()
        while(userBars != "default" and userBars < 1 ):
            print("Sorry, but your input doesn't meet the criteria given above. Please try again.")
            userBars = input()
        if(userBars is "default"):
            userBars = 1
        
            
        print("Do you wish to change the velocity or retain the default settings? (Enter with 'change' or 'default'. ")
        velDefault = input()
        if(velDefault is "default"):
            isRandVelocity = False
            velocity = 100
        elif(velDefault is "change"):
            print("Do you want the velocities to be random or constant? (Enter with 'r' or 'c')")
            userVel = input()
            if(userVel is 'r'):
                velVal = random.randrange(0, 127)
            elif(userVel is 'c'):
                print("Please enter the value of the velocity. (Enter as an integer between 1 and 127)")
                velVal = input()
                while(velVal > 127 and velVal < 1):
                    print("Velocity is out of range, try again.")
                    velVal = input()
                isRandVelocity = True
            else:
                while(userVel != 'r' and userVel != 'c'):
                    print("Please enter the character 'r' or the character 'c'.")
                    userVel = input()
        else:
            while(velDefault != "default" and velDefault != "change"):
                print(" Sorry but neither of the two choices were picked, so your input doesn't meet the criteria given above. Please try again.")
                velDefault = input()
                
        print("Enter your preferred tempo or choose to retain default settings.")
        userTemp = input()
        if(userTemp is 'default'):
            userTemp = 120
        elif(userTemp > 999 or userTemp < 20):
            while(userTemp > 999 or userTemp < 20):
                print("The value entered is out of range, please try again.")
                userTemp = input()
        bars = userBars
        vel = userVel
        scale = "na"
        temp = userTemp