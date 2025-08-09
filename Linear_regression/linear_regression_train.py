
import random

class Linear_Regression:
    def __init__(self,number_records,lr=0.001):
        self.w=random.randrange(1,3)
        self.b=random.randrange(1,3)
        self.loss=0
        self.train_b=0

        self.lr=lr
        self.n=number_records

    def forward(self,X,y):
        self.x=X
        y1=self.w*self.x+self.b
        self.gradient_mse(y1,y)

    def gradient_mse(self,actual,target):
        # print("actual:",actual,"target:",target)
        loss=self.x*(actual-target)
        b=(actual-target)
        self.loss+=loss
        self.train_b+=b
    def gradient_update(self):
        self.w=self.w-self.lr*(2*self.loss/self.n)
        self.b=self.b-self.lr*(2*self.train_b/self.n)
    def pred_(self,inp):
        y1=self.w*inp+self.b
        print("predicted output:",int(y1))
        return round(y1)




x=[1,3,4,5]
y=[0,2,3,4]
epoches=10000
test=Linear_Regression(len(x))
test.lr=0.01
count=1
# while True:
print("count",count,"epoches :",count*epoches)
for epoch in range(epoches):

    for i in range(len(x)):

        test.forward(x[i],y[i])
    test.gradient_update()
    test.loss=0
    test.train_b=0

# if y[0]==test.pred_(x[0]):
#     break
count+=1
for i in range(len(x)):
   print("x,y,pred",x[i],y[i],test.pred_(x[i]))









        
