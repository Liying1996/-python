class HMM:

	def __init__(self, trans, emis, primary, state):
		self.trans = trans      # transition probability
		self.emis = emis        # emission probability
		self.primary = primary  # primary probability
		self.state = state      # observed state
	
    
	def forward(self):
		self.all_pro = array(zeros((len(self.state), len(self.trans))))

		# when t = 1:
		self.all_pro[0] = self.primary * self.emis[:,self.state[0]] 

		# From t = 2 until end
		for j in range(1, len(self.state)):
			self.all_pro[j] = (self.all_pro[j - 1] * self.trans.T).sum(axis = 1) * self.emis[:, self.state[j]]

		# for k in range(len(x)):
		# 	print("when t = {} : ".format(k))
		# 	print(x[k])

		return "The final Probability is : {}".format(sum(self.all_pro[-1]))
