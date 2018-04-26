# 2018_Earlham_Cap
1. Python modules required: scikit-learn, numpy
2. Data File
   - data.csv contains sensor collected conditions value(humidity, temperature, light)
   - ratio.csv contains the growth rate of the plant
   - actuallength.csv contains the length of the plant
3. Data collecting code
   - Arduino_data_Collect.ino modifies the arduino sensors and outputs raw data
   - data_collect.py collects raw data from Arduino_data_Collect.ino and outputs into a csv file
4. Naive Bayes
   - test.py tests the validity of Naive Bayes
   - Naive_Bayes.py takes 2 csv files(condition values, growth rate), and predict with given conditions
5. Plot
   - plot.py generates relational diagrams of each conditions with growth rate.
Notes:
   - Run Naive_Bayes.py, it will load both condition and ratio file.
   
   - Although I have spend weeks working on Naive Bayes, but there is a bug in Naive_Bayes.py. However, test.py has the exactly the same strucutre and data type, it worked perfectly fine. I have consulted with my project advisor, Daivd Barbera, but no soultion yet. I may need to come back to fix this bug in the future.
