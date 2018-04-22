import midi
import random
import GenerateFile

class Prompt:
    
    def __init__(self, bars, isVel, vel, scale, tempo):
        userBars = ""
        #default = 1
        velDefault = ""
        userVel = ""
        #default = 100
        velVal = 0
        userSca = ""
        userTemp = ""
        print("Enter the number of bars/measures, or choose to retain default settings. (Enter as an integer value or enter 'default')")
        userBars = raw_input()
        while(userBars != "default" and userBars < 1 ):
            print("Sorry, but your input doesn't meet the criteria given above. Please try again.")
            userBars = raw_input()
        if(userBars is "default"):
            userBars = 1
        
            
        print("Do you wish to change the velocity or retain the default settings? (Enter with 'change' or 'default'. ")
        velDefault = raw_input()
        if(velDefault is "default"):
            isRandVelocity = False
            velVal = 100
        elif(velDefault is "change"):
            print("Do you want the velocities to be random or constant? (Enter with 'r' or 'c')")
            userVel = raw_input()
            if(userVel is 'r'):
                velVal = random.randrange(0, 127)
            elif(userVel is 'c'):
                print("Please enter the value of the velocity. (Enter as an integer between 1 and 127)")
                velVal = raw_input()
                while(velVal > 127 and velVal < 1):
                    print("Velocity is out of range, try again.")
                    velVal = raw_input()
                isRandVelocity = True
            else:
                while(userVel != 'r' and userVel != 'c'):
                    print("Please enter the character 'r' or the character 'c'.")
                    userVel = raw_input()
        else:
            while(velDefault != "default" and velDefault != "change"):
                print(" Sorry but neither of the two choices were picked, so your input doesn't meet the criteria given above. Please try again.")
                velDefault = raw_input()
                
        print("Enter if you wish to change the tempo, or choose to retain default settings. (Please enter '1' to change the settings or '0' to retain the default settings)" )
        tempo = input()
        while(tempo != 0 and tempo != 1):
            print("You didn't enter the correct response, try again.")
            tempo = input()
        if(tempo == 0):
            userTemp = 120
        elif(tempo == 1):
            print("Enter your desired tempo.")
            userTemp = input()
        
            
            
            
            
            
            '''
        elif(userTemp > 999 or userTemp < 20):
            while(userTemp > 999 or userTemp < 20):
                print("The value entered is out of range, please try again.")
                userTemp = raw_input()
            '''
        bars = userBars
        vel = velVal
        scale = "na"
        temp = userTemp