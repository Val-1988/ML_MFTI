class Neuron:

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.f = f
        self.x = None

    def forward(self, x):
        self.x = x
        self.wx = [self.w[i] * self.x[i] for i in range(len(self.w))]
        print(self.wx)
        #B = [elem for elem in [sum(A[0:i[0]]) for i in enumerate(A, 1)]]
        return self.wx

    def backlog(self):
        return self.x

a = Neuron([1,2,3], Neuron.forward([1,2,3]))
print(a)
a.forward([1,2,3])
