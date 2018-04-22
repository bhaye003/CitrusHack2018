import midi
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
print pattern
# Save the pattern to disk
midi.write_midifile("example.mid", pattern)
