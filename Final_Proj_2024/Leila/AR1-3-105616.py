# This program takes three values from a CSV file and compares them to predict a fourth value
# This program then attempts to execute a "Multiple Linear Regression" AR1
# using 3 independent variables and one dependent variable.       AR1
# The program uses input parameters from the user to make a prediction   AR1
# The program the considers a number of WHAT-IF scenarios using the "trained" model AR2
# to make further predictions
# The program then produces the outcomes from above in a graphical format   AR3
# My program is processing a dataset that originates from an embedded system which senses light
# and uses that data along with user input to test/train a model which predicts mood
# Some Standards: All functions will be at the top of the code, All import statements will be at the top of the code

#Import Statements
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Prediction function to predict using 3 independent variables and one dependent variable. 
def predict_mood(hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity):
    df = pd.DataFrame([[hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity]],
                      columns=['Hours_Light', 'Intensity_Light', 'Peak_Light'])
    return my_model.predict(df)[0]
#################### The Data Modelling ################### AR1
# Training the model
# first Load your dataset , a copy of output from BR1-3 to keep original data from BR1-3
data = pd.read_csv('AR1-3-105616.csv') # This dataset is a copy of the output from BR1-3, copied so as to create a backup of BR1-3 data

# Define your independent variables (features) and dependent variable (target)
X = data[['Hours_Light', 'Intensity_Light', 'Peak_Light']]
Y = data['Mood_Score']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
my_model = LinearRegression()

# Fitting the model with the training data
my_model.fit(X_train, Y_train)

# Predicting mood scores for the test set
Y_pred = my_model.predict(X_test)


print("My Multiple Linear Regression Model is now Complete!")
####################### Data Modelling complete #################### AR1

############  Testing the Model ################### AR1
# Making a prediction using the model
# Let the user enter their own 3 parameters
# Note 2 different datatypes
print("")
print("USER CHOOSES 3 LIGHT LEVELS MODE")
hours = int(input("Enter sunlight hours. Can be any integer from 0-24 "))
sun = float(input("Enter average sunlight intensity. Can be anything from 1-800 "))
peak = float(input("Enter peak sunlight level. Can be anything from 1-800 "))

################## Tested the model############################
# Data: names of the variables and their values for the Bar Chart    AR3
#------------------------------------
# AR3 Users can view data in a graphical format which displays information such as their progress
#using the system or the results of a ‘what if’ scenario.

# Data: names of the variables and their values for the chart
variable_names = ['Hours of Sun', 'Peak Sun','Average Sun']
values = [hours,peak,sun]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Ammount of Sun')
plt.ylabel('Mood')
plt.title('Bar Chart of sun measurement')

# Show the plot
plt.show()
#Predict the mood based on input values 
predicted_mood = round(predict_mood(hours, sun, peak),2)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)
