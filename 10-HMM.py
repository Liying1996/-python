class HMM:

    def __init__(self, A, B, PI, obs, V, Q):
        self.A = A              # Aition probability
        self.B = B           # Bsion probability
        self.PI = PI  # PI probability
        self.obs = obs      # observed obs
        # v为观测集合，如{红，白}; q为状态序列，如{盒子1,盒子2,盒子3,盒子4}
        self.V = V
        self.Q = Q
    
    def forward(self):
        self.all_for = zeros((len(self.obs), len(self.A)))

        # when i = 1:
        self.all_for[0] = self.PI * self.B[:,self.V.index(self.obs[0])] 

        # From i = 2 until end
        for j in range(1, len(self.obs)):
            self.all_for[j] = (self.all_for[j - 1] * self.A.T).sum(axis = 1) * self.B[:, self.V.index(self.obs[j])]

        print(self.all_for)
        # print(sum(self.all_for[k]))

        return "The forward final Probability is : {}".format(sum(self.all_for[-1]))


    def backward(self):
        self.all_back = zeros((len(self.obs), len(self.A)))

        # when i = -1:
        self.all_back[-1] = array([1] * len(self.PI))

        # when i = -2 until PI:
        for j in range(len(self.obs) - 2, -1, -1):
            self.all_back[j] = (self.all_back[j + 1] * self.A * self.B[:,self.V.index(self.obs[j + 1])]).sum(axis = 1)

        print(self.all_back)

        return "The backward final Probability is : {}".format(sum(self.all_back[0] * self.PI * self.B[:,self.V.index(self.obs[0])]))


    def veterbi(self):

        N = len(self.Q)
        T = len(self.obs)
        delta = zeros((T,N), dtype='float64')
        phi = zeros((T,N), dtype='int')

        delta[0, :] = PI * B[:, self.V.index(obs[0])] # 初始

        for i in range(1, T ): # 1,2,3
            tmp1 = []
            tmp2 = []
            for j in range(N): # 0,1,2
                tmp1.append(max(delta[i - 1,:] * A[:, j] * B[j, self.V.index(obs[i])]))
                tmp2.append(argmax(delta[i - 1,:] * A[:, j] * B[j, self.V.index(obs[i])]))
            delta[i,:] = array(tmp1)
            phi[i,:] = array(tmp2)
        # print(delta, '\n', phi)

        path = [phi[-1, argmax(delta[-1, :])]] # 最终节点
        for k in range(T - 1, 0, -1): # 倒着的path
            path.append(phi[k, path[-1]])

        hidden = [self.Q[m] for m in reversed(path)]
        return hidden
    
 	
	
# 10.1  the result is 0.06009079999999999
A = array([(0.5,0.2,0.3),(0.3,0.5,0.2),(0.2,0.3,0.5)]) 
B = array([(0.5,0.5),(0.4,0.6),(0.7,0.3)])
PI = array([(0.2),(0.4),(0.4)])
obs = ["红", "白", "红", "白"]
Q = [1, 2, 3]
V = ["红", "白"] 
HMM(A ,B, PI, obs, V, Q).backward()

# 10.2  According to the 10.24 formula in P179, the result is: 
# 0.04280618(backward) * 0.04361112(forward) / 0.0034767 = 0.53695181
 
# 10.3
HMM(A ,B, PI,obs, V, Q).veterbi()
# 结果为[3, 2, 2, 2]
