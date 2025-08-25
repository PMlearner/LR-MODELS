from tqdm import tqdm
from activation_fn import sigmoid
import math,random

class Logistic_Regression:
    def __init__(self,number_features,epoches,lr):
        self.number_features=number_features
        self.epoches=epoches
        self.lr=lr
        self.w,self.b=[random.randrange(1,3) for i in range(number_features)],random.randrange(1,3)
        self.db=0
        self.dw=[0]*self.number_features
    def forward(self,X,Y):
        self.n=len(X)
        for epoch in tqdm(range(self.epoches)):

            print("Epoch:",epoch)
            for x in range(len(X)):
                y=sum([self.w[i]*X[x][i] for i in range(self.number_features)])+self.b
                output=sigmoid(y)
                self.gradient_binary_cross_entropy(Y[x],output,X[x])
            self.gradient_update()






    def gradient_binary_cross_entropy(self,target,output,_input):
        # error=(1/self.n)*sum(target*math.log(output)+(1-target)*(math.log(1-output))) # This is Binary cross entropy we need to find the gradient
        error=output-target # Gradient in logistic just need to calculate the different between actual and target
        self.dw=[self.dw[i]+error*_input[i] for i in range(self.number_features)]
        self.db+=(output-target)

    def gradient_update(self):
        # self.w=[self.w[i]-(self.lr*(2*self.dw[i]/self.n)) for i in range(self.number_features)]#for mse we need that 2 
        self.w=[self.w[i]-(self.lr*(self.dw[i]/self.n)) for i in range(self.number_features)]#binary cross entropy we dont needed this 2
        for i in range(len(self.dw)):
            self.dw[i]=0
        self.b=self.b-(self.lr*(self.db/self.n))
        self.db=0
    def pred(self,X):
 
            y=sum([self.w[i]*X[i] for i in range(self.number_features)])+self.b
            output=sigmoid(y)
            return output




    







