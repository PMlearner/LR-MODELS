
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
        print("predicted output:",y1)
        return round(y1)
class Linear_Regression_multifeature:
    def __init__(self,number_records,lr=0.05,number_features=1):
        self.w=[random.randrange(1,3) for i in range(number_features)]
        self.b=random.randrange(1,3)
        self.features=number_features
        self.loss=[0]*number_features
        self.train_b=0

        self.lr=lr
        self.n=number_records

    def forward(self,X,y):
        self.x=X
        y1=sum((self.w[i]*self.x[i] for i in range(self.features)))+self.b
        self.gradient_mse(y1,y)

    def gradient_mse(self,actual,target):
        # print("actual:",actual,"target:",target)
        loss=[self.x[i]*(actual-target) for i in range(self.features)]
        b=(actual-target)
        self.loss+=loss
        self.train_b+=b
    def gradient_update(self):
        self.w=[self.w[i]-self.lr*(2*self.loss[i]/self.n) for i in range(self.features)]
        for i in range(self.features):
            self.loss[i]=0
        self.b=self.b-self.lr*(2*self.train_b/self.n)
        self.train_b=0
    def pred_(self,inp):
        y1=sum((self.w[i]*inp[i] for i in range(self.features)))+self.b
        print("predicted output:",y1)
        return round(y1)




x=[1,3,4,5]
y=[0,2,3,4]
epoches=5000
#--------------------------------------------------------------------single feature----------------------------------------------------------------

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
print("x,y,pred",15,14,test.pred_(15))

#--------------------------------------------------------------------multi features----------------------------------------------------------------
import pandas as pd
# df=pd.read_csv('Boston.csv')
# print(df.shape[1])
# df = df.iloc[:, 1:]
# train=df[:406].iloc[:, :-1]
# train_target= df[:406].iloc[:, -1]
# print(train.shape)
# test=df[407:].iloc[:,:-1]
# test_target=df[407:].iloc[:,-1]

# obj=Linear_Regression_multifeature(train.shape[0],number_features=train.shape[1])
# # while True:
# # print("count",count,"epoches :",count*epoches)
# train_data=train.values
# from tqdm import tqdm
# print(train)

# for epoch in tqdm(range(epoches)):
    
#     # print("epoch",epoch+1)
#     for i in range(train.shape[0]):

#         obj.forward(train_data[i],train_target[i])
#     obj.gradient_update()
#     # obj.loss=0
#     # test.train_b=0

# # if y[0]==test.pred_(x[0]):
# #     break
# # count+=1
# for i in range(test.shape[0]):
#     x_row = test.iloc[i].to_numpy()  # get i-th row as numpy array
#     y_true = test_target.iloc[i]     # get i-th target value
#     y_pred = obj.pred_(x_row)        # predict
#     print("x,y,pred", x_row, y_true, y_pred)





        
