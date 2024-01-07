# This program takes three values from a CSV file and compares them to predict a fourth value
# This is given the fancy name "Multiple Linear Regression".
# It's like a bunch of linear trendlines mashed up together to allow a few more extra variables.

# HOW TO USE:
# Thonny>Tools>Manage Packages and install sklearn, pandas
# Open the CSV file called "your_dataset" in the same folder as this python file
# Replace my columns of data with your data
# Change the titles of each of my columns to your own titles
# Do the same in the code below

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#
#
#THE PROGRAM CAN ONLY WORK WITH INTEGER/FLOAT DATA, STRINGS WILL CAUSE PROBLEMS
#
#
# Training the model

# Load your dataset THIS DATA HAS STRING DATA
data = pd.read_csv('Tennis.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['Day', 'Outlook', 'Temp', 'Humidity', 'Wind']]
Y = data['Play']

#print("X, Y Data",type(X),type(Y),X,Y)

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# Creating the Linear Regression model
#creating an instance of the LinearRegression class from scikit-learn
model = LinearRegression()
# Fitting the model with the training data
# WHEN YOU TRY TO FIT THA STRING DATA INTO THE MODEL IT CRASHES
model.fit(X_train, Y_train)
# Predicting mood scores for the test set
#Y_pred = model.predict(X_test)