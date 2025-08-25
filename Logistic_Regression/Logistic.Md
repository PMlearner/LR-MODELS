Logistic Regression:
    1.Same as Linear Regression in end we change the loss function and adding a sigmoid function based on that it idenitfy the output like only binary classification
    2.We have several different Logistic regression models for multiclass it called multinominal logistic Regression and ovr(one vs rest) or ova(one vs all)
    3.Here loss we are using the Binary cross entropy or Log loss
       Binary cross entropy=-1/n(sum of ([target(log(actual))+(1-target)log(1-actual))]))

       Gradient Calculation:
         derivative by output= -target/actual+1-target/1-actual
         here 