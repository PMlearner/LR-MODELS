Cross Entropy:
    Basically cross entropy will use for find the catergorical data like cat or dog
    Binary cross entropy:
        after getting sigmoid probablietes we are checking with those classes and identiy the proper loss based on this we will update the wieghts using that next time it will identify the proper class in modle itself
    Categorical cross entropy:
        Here we have multiple classess we are getting multiple probalites like if three class have then we getting three list of probablites using softmax we need to check with each class identify which one gives higher probabilites 

        =-sum(target*log(actual)) for number of classess



Categroical cross entropy:

Here we getting proballites of each class outputs from softmax activation function like [0.1,0.2,0.4]
next we need to calcualte cross entropy here formula for this =-1/n(sum of each input(sum of each class((mn)*log(probality of that value))))

here consider we have three class each class like if first class then  
mn - value for that class is (one hot) 1 other class is 0


here you getting each class probality and average of that class log probality as a loss
