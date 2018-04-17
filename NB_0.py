import csv
import numpy as np
from sklearn.naive_bayes import GaussianNB
#datareader = csv.reader(open("data.csv","rb"),delimiter=',')
X = np.genfromtxt('data.csv',delimiter=',',dtype=np.float64, names=None)
#lengthreader = csv.reader(openopen("actuallength.csv","rb"),delimiter=',')
Y = np.genfromtxt('ratio.csv',delimiter=',',dtype=np.float64, names=None)
gnb = GaussianNB()
for i in range(10):
	print(X[i])
	print(Y[i])
gnb.fit(X,Y)
print(gnb.predict([[623,22,43]]))
