import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB
#datareader = csv.reader(open("data.csv","rb"),delimiter=',')
X = np.array([[-1, -1,0], [-2, -2,-1], [-3,-3, -2], [1, 1,1], [2, 1,1], [3, 2,2]])

#lengthreader = csv.reader(openopen("actuallength.csv","rb"),delimiter=',')
Y = np.array([1, 1, 1, 2, 2, 2])
for i in range(3):
	print (X[i])
	print (Y[i])
gnb = GaussianNB()
gnb.fit(X,Y)
print(gnb.predict([[1,1,1]]))
