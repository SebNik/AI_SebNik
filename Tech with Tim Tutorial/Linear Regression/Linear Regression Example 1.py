import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

# opening the data
data = pd.read_csv("student-mat.csv")
# only reading in interesting columns
data = data[["G1", "G2", "G3", "studytime", "failures", "absences", "freetime", "traveltime", "age"]]

predict = "G3"

X = np.array(data.drop([predict], 1))  # Features
y = np.array(data[predict])  # Labels

# splitting up in to the train and test sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1, random_state=0)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)  # acc stands for accuracy

print('Accuracy: \n', acc)

print('Coefficient: \n', linear.coef_)  # These are each slope value
print('Intercept: \n', linear.intercept_)  # This is the intercept


predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])