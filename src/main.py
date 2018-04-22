import midi
import random
# Instantiate a MIDI Pattern (contains a list of tracks)


while(1):
	print("Menu\n1) Generate File\n2)Options\n3)exit\n\n")
	response = input()

	if response == 1:
		midiFile = FileGenerator();
	elif response == 2:
		print("ITEM 2")
	elif response == 3:
		print("Thanks for using Inspiration")
		exit()
	else:
		print("Invalid number, please enter again...\n")


def ranNote(self):
    ranKey = random.randrange(0,13)
    ranOct = random.randrange(0,13)
    ranKey = chr(ranKey + 65)
    ranTick = random.randrange(0,100)
    newPitch = ranKey + "_" + ranOct
    
    return midi.NoteOnEvent(tick = ranTick, velocity = 100, pitch = midi.newPitch)



    



def FileGenerator():
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
    
    
    print("Do you wish to change the scale or retain the default settings? (Enter with 'change' or 'default'. ")
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
        
            
    #print("Enter your preferred scale or choose to retain the default settings. (Enter 'default' or integer between 20 and 999)")
    #userSca = input()
   
    
'''        
    pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
    track = midi.Track()
# Append the track to the pattern
    pattern.append(track)
# Instantiate a MIDI note on event, append it to the track
    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=midi.G_3)
    track.append(on)
# Instantiate a MIDI note off event, append it to the track
    off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
    track.append(off)
# Add the end of track event, append it to the track    
    eot = midi.EndOfTrackEvent(tick=1)
    track.append(eot)
# Print out the pattern
#print pattern
# Save the pattern to disk
'''
