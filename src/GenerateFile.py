import midi

class GenerateFile:

	def __init__(self, bars=1, tempo=120, isRandVelocity=True, velocity=100):
		self.bars = bars
		self.tempo = tempo
		self.isRandVelocity = isRandVelocity
		self.velocity = velocity

	def generate()
		pattern = midi.Pattern()
		track = midi.Track()

		curr_ticks = 0
		while(curr_ticks < tempo):
			

