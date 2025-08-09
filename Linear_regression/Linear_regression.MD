LINEAR REGRESSION:
   This is the algorithm when regression like continues data (data contains numerical values) 
   Here We try to draw best line based on the datapoint(like average line for all datapoints)
   It used the train data output as target and predict the value using input and find the error by gradient loss

   How is it find the w based on loss:
   1.using y=wx+b---> find the output(y^)

   2.Next we need to find the loss here so based on MSE(Mean Squared Error) its =1/n(sum of actual-target)**2


   3.There step 2 we got loss,Loss just the error we didnt know which direction  loss happened for that we are using gradient

   4.Gradient like ∂Loss/∂w   here we have  loss right so try to defferentiate a loss by w ,here instead of actual we replace the straight line form y=wx+b--->so its  {2/n(sum of each input*(output-target))}

   5.we getting gradient loss so now we will update the weights w= w(old)-lr*gradient loss

   Loss Functions:

   For regression we have certain functions we can you any one of those there some function perfoms well for the certain cases based on the data using this is giving a better results when Training Model

   MAE---1/n sum of |actual-target|(absolute mean it just mention the value not the distance also its non negative)

   RMSE---root of mse  



    For Bias update same as gradient only thing is leave input data in calculating Gradient {2/n(sum of each (output-target))}


    N Features:
    In each feature have certain w ,it will update independently one another last sum all the feature with common bias
    like y=w1*x1+w2*x2+b only​