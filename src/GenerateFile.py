import midi
import random
import Prompt

class GenerateFile:

	#def __init__ (self, *args, **kwargs):
	def __init__(self, bars=4, tempo=120, velocity=100):
		self.bars = bars
		self.tempo = tempo
	#	self.isRandVelocity = isRandVelocity
		self.velocity = velocity

	def generateMono(self):
		pattern = midi.Pattern()
		track = midi.Track()
		curr_ticks = 0
		max_ticks = 1000 * self.bars
		t = midi.SetTempoEvent()
		t.set_bpm(self.tempo)

		pattern.append(track)

		while(curr_ticks < max_ticks):			
			space = random.randrange(0, 101)
			p = self.generateChar();
			insertNote = midi.NoteOnEvent(tick=curr_ticks, velocity=self.velocity, pitch=p)
			if max_ticks < space + curr_ticks:
				space = max_ticks - curr_ticks
			else:
				curr_ticks += space
			track.append(insertNote)
			endNode = midi.NoteOffEvent(tick=curr_ticks, pitch=p)
			track.append(endNode)
		eot = midi.EndOfTrackEvent(tick=1)
		track.append(eot)
		userString = raw_input("Please enter the file name:")
		midi.write_midifile(userString, pattern)


	def generateChar(self, isScale=None):

			if(isScale == None):

				note = random.randrange(0, 13)
				if(note == 0):
					nChar = "A_" 
				elif(note == 1):
					nChar = "As_"
				elif(note == 2):
					nChar = "B_" 
				elif(note == 3):
					nChar = "C_" 
				elif(note == 4):
					nChar = "Cs_"
				elif(note == 5):
					nChar = "D_"
				elif(note == 6):
					nchar = "Ds_"
				elif(note == 7):
					nChar = "E_"
				elif(note == 8):
					nChar = "F_"
				elif(note == 9):
					nChar = "Fs_"
				elif(note== 10):
					nchar = "G_"
				else:
					nchar = "G_s"

				octave = random.randrange(4, 10)
				retNote = note + octave
				return retNote



			


