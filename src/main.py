import midi
import random
# Instantiate a MIDI Pattern (contains a list of tracks)


while(1):
	print("Menu\n1) Generate File\n2)Options\n3)exit\n\n")
	response = input()

	if response == 1:
		pattern = midi.Pattern()#resolution = (60 * 1000000 / bpm))
		
		track = midi.Track()
		pattern.append(track)

		on = midi.NoteOnEvent(tick = 0, velocity = 20, pitch=midi.A_3)
		track.append(on)
		
		on = midi.NoteOnEvent(tick = 1, velocity = 20, pitch=midi.B_3)
		track.append(on)

		off = midi.NoteOffEvent(tick = 120, pitch=midi.A_3)
		track.append(off)

		off = midi.NoteOffEvent(tick = 120, pitch=midi.B_3)
		track.append(off)
		
		eot = midi.EndOfTrackEvent(tick = 1)
		
		track.append(eot)

		print pattern
    	midi.write_midifile("example.mid", pattern) 
