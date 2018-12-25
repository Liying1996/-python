class HMM:

	def __init__(self, trans, emis, primary, state):
		self.trans = trans      # transition probability
		self.emis = emis        # emission probability
		self.primary = primary  # primary probability
		self.state = state      # observed state
	
    
	def forward(self):
		self.all_for = array(zeros((len(self.state), len(self.trans))))

		# when i = 1:
		self.all_for[0] = self.primary * self.emis[:,self.state[0]] 

		# From i = 2 until end
		for j in range(1, len(self.state)):
			self.all_for[j] = (self.all_for[j - 1] * self.trans.T).sum(axis = 1) * self.emis[:, self.state[j]]

		# print(self.all_for)

		return "The final Probability is : {}".format(sum(self.all_for[-1]))
