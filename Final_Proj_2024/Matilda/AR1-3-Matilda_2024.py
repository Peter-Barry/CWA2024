# My program takes three different values from my CSV file I created and compares them with eachother to predict a fourth value
# It then executes a "Multiple Linear Regression" (AR1)
# My program uses 3 different input parameters from the user to make the prediction (AR1)
# My program then utilises WHAT-IF scenarios using the "trained" model (AR2) to make further predictions
# The results from above are then produced in graphical format   AR3
# My program is processing a dataset that originates from an embedded system which senses temperature
# It uses these results and data along with inputs from the user to test/train a model which predicts your mood
# Standards I followed for all: All functions will be at the top of the code, All import statements will be at the top of the code


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Prediction function to predict using 3 independent variables and one dependent variable. 
def predict_mood(hours_of_temperature, temperature_intensity, peak_temperature_intensity):
    df = pd.DataFrame([[hours_of_temperature, temperature_intensity, peak_temperature_intensity]],
                      columns=['Temperature_min', 'Temperature_max', 'Temperature_mean'])
    return model.predict(df)[0]

#Loading in my data set
data = pd.read_csv('AR1-3_results105716.csv')

# Defining my independent and dependant variable 
X = data[['Temperature_min', 'Temperature_max', 'Temperature_mean']]
Y = data['Average mood']
 
# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model (AR1)
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)

# Predicting mood scores for the test set
Y_pred = model.predict(X_test)


print("My Multiple Linear Regression Model is now complete!")

# Making a prediction using the model
# The user inputs their own 3 parameters (AR1)
# 2 different datatypes being used 
print("")
print("USER CHOOSES 3 TEMPERATURE LEVEL MODES")
hours = int(input("Enter the number of hours over which you measured the temperature. Can be any integer from 0-24 "))
temp = float(input("Enter average temperature intensity. Can be anything from 1-12 "))
peak = float(input("Enter peak temperature level. Can be anything from 1-34 "))
# As we live in Ireland, the range values were much lower than they would be in a hotter country.

predicted_mood = predict_mood(hours, temp, peak)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)


# WHAT IF QUESTIONS (AR2)
# WHAT-IF Question 1
# What will the mood be with low value inputs for all three of the parameters?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 1")
print("'Let's test what the mood will be if the temperature is very low'")

# Low values for all 3 parameters
temperature_hours = 4
average_temperature = 2
peak = 4

mood_if_littleTemp = predict_mood(temperature_hours, average_temperature, peak)  # Example values
print("\n The low temperature score mood is", mood_if_littleTemp)



# WHAT-IF Question 2
# What will the mood be with high values for all three of the parameters?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 2")
print("'Let's test what the mood will be if the temperature is very high'")

# High values for all 3 parameters
temperature_hours = 23
average_temperature = 12
peak = 33

mood_if_highTemp = predict_mood(temperature_hours, average_temperature, peak)  # Example values
print("\n The higher temperature score mood is", mood_if_highTemp)



# WHAT IF QUESTION 3
# What will the mood be with normal/average values for all three of the parameters??
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 3")
print("'Let's test what the mood will be with average temperature'")
print("We will keep the hours (A) the same and double the others (B) and (C) one at a time")
print("")

print("Let's get a baseline from fairly average values...")

# Average values for all 3 parameters 
temperature_hours = 13
average_temperature = 8
peak = 25

mood_if_Averagetemp = predict_mood(temperature_hours, average_temperature, peak)  # Example values
print("\nThe average temperature score mood is", mood_if_Averagetemp)
print("")

# Data: names of the variables and their values for the Bar Chart (AR3)
#------------------------------------
# User can view data and results in a graphical format which displays information such as their progress
# using the system or the results of a ‘what if’ scenario.
# Data: names of the variables and their values for the chart
variable_names = ['Mood if high temp', 'Mood if normal temp','Mood if low temp']
values = [mood_if_littleTemp, mood_if_Averagetemp,mood_if_highTemp]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('[Temperature]')
plt.ylabel('[Mood]')
plt.title('Bar Chart of all 3 WHAT-IFs Predictions')

# Show the plot
plt.show()