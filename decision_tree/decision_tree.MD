CLASSIFICATION:
    when data comes we will split featurs and lables first after that in features each clms we will check if categorical or continuos same time we will callculate the parent (gini or entropy )impurity value

    once figure that for categorical data combine the all the class like if we have 4 different class then each class how many records /totall number of class for each class in that  we able to identify the the each call values then 1- (sum of all the (classes is the impurity)**2)

    For continuous data here we  sorting the datas and find the out the each records mid values for next one of that data and in those data pic the middle value based on that we   caluculat the impurity then 

    after finding the impurity of the layere of each layer already we have  impurity of the labled clm using that we will figure out the each features IG(information gain )=impurity of partent -impurity of futures here which ig if high using that we will split the features left and right same approach based on the data will figure out the which based need to split everything is 0 or equal stop the spliting and thats the leaf node voting based we will select the target


    here each  step for Impurity of that node need to calculate for information gain (because information gain is the threshold for when testing ) here for calculating the entire step impurity we have calculathe by

    impurity of that step to split =(number of class in left/number of total class)*impurity of that feature in left+same of right
    One thing impurity of the parent node is calculated unique for each node


FOR REGRESSION:
    in impurtiy calculation instead of using gini and entropy we will use the variance or mse for 


    so the calculation is like Impurity for each features = 1/n(sum((y-mean(target))**2))
    impurity of that step to split =(number of class in left/number of total class)*impurity of that feature in left+same of right

