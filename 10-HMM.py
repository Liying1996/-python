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
	
	
	def backward(self):
		self.all_back = array(zeros((len(self.state), len(self.trans))))

		# when i = -1:
		self.all_back[-1] = array([1] * len(self.primary))

		# when i = -2 until primary:
		for j in range(len(self.state) - 2, -1, -1):
			self.all_back[j] = (self.all_back[j + 1] * self.trans * self.emis[:,self.state[j + 1]]).sum(axis = 1)

		print(self.all_back)

		return "The final Probability is : {}".format(sum(self.all_back[0] * self.primary * self.emis[:,self.state[0]]))
	
	
	
	
	
# 10.1  the result is 0.06009079999999999
trans = array([(0.5,0.2,0.3),(0.3,0.5,0.2),(0.2,0.3,0.5)]) 
emis = array([(0.5,0.5),(0.4,0.6),(0.7,0.3)])
primary = array([(0.2),(0.4),(0.4)])
state = [0, 1, 0, 1]
HMM(A,B,pri,o).backward()

# 10.2  According to the 10.24 formula in P179, the result is: 
# 0.04280618(backward) * 0.04361112(forward) / 0.0034767 = 0.53695181
 	
