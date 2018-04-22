import midi
import Prompt
import GenerateFile
import random
# Instantiate a MIDI Pattern (contains a list of tracks)

__tempo = 120
__bars = 1
#__isVel = False
__vel = 100
__scale = "na"
__tempo = 120

while(1):
	print("Menu\n1) Generate File\n2)Options\n3)exit\n\n")
	response = input()

	if response == 1:
		midiFile = GenerateFile.GenerateFile(__bars, __tempo, __vel)
		midiFile.generateMono
	elif response == 2:
		
		message = Prompt.Options(__bars, __vel, __scale, __tempo)
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



    



#def FileGenerator():
    
        
            
    #print("Enter your preferred scale or choose to retain the default settings. (Enter 'default' or integer between 20 and 999)")
    #userSca = input()
   
