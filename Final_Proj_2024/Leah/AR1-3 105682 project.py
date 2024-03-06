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

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# All functions at the top of the code
# Function to pass parameters to the model and get a prediction
def predict_mood(hours_of_sound,average_sound , peak_sound):
    df = pd.DataFrame([[hours_of_sound,average_sound , peak_sound]],
                      columns=['Hours_sound', 'Average_sound', 'Peak_sound'])
    return model.predict(df)[0]
#Function to get the input from the screen
def get_user_input():
    hours = int(input("Enter hours of sound. Can be any integer from 0-24 "))
    sound = float(input("Enter average sound intensity. Can be anything from 1-194 dB ")) #dB means decibels
    peak = float(input("Enter peak sound level. Can be anything from 1-194 dB "))
    return hours, sound, peak
# Training the model

# Load your dataset
data = pd.read_csv('AR1-3_input.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['Hours_sound', 'Average_sound', 'Peak_sound']]
Y = data['Mood_Score']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)

# Predicting mood scores for the test set
Y_pred = model.predict(X_test)


print("Multiple Linear Regression Model Complete!")

# Making a prediction using the model
# Let the user enter their own 3 parameters
# Note 2 different datatypes
print("")
print("USER CHOOSES 3 SOUND LEVELS MODE")

print("USER CHOOSES 3 LIGHT LEVELS MODE CALLING FUNCTION get_user_input")
hours, sound, peak = get_user_input()

predicted_mood = round(predict_mood(hours, sound, peak),2)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)

#___________________What If Questions AR2 _________
# WHAT-IF Q1
# What is will your mood be with low values given to the 3 params?

print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 1")
print("Let's test what the mood will be if the sound is very low")

# Low values for all 3 parameters
mood_if_littleSound = round(predict_mood(1,3,7),2)  # Example values
print("\n The low sound score mood is", mood_if_littleSound)

# WHAT-IF Q2
# What is will your mood be with high values given to the 3 params?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 2")
print("Let's test what the mood will be if the sunlight is very high")
mood_if_highSound = round(predict_mood(22, 185, 190),2)  # Example values
print("\n The higher sound score mood is", mood_if_highSound)

# WHAT IF Q3
# # What is will your mood be with middle/normal values given to the 3 params?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 3")
print("Let's test mood if medium sound")

# middlin values for all 3 parameters 
mood_ifmediumSound = round(predict_mood(11,95,100),2)  # Example values
print("\n The middle sound Score mood is", mood_ifmediumSound)
print("")

#------------------------------------
# AR3 Users can view data in a graphical format which displays information such as their progress
#using the system or the results of a ‘what if’ scenario.

# Data: names of the variables and their values for the chart
variable_names = ['Mood if Little Sound', 'Mood if High Sound', 'Mood if Medium Sound']
values = [mood_if_littleSound, mood_if_highSound, mood_ifmediumSound ]
# Creating the bar chart
plt.bar(variable_names, values)
# Adding labels and title
plt.xlabel('Amount of sound')
plt.ylabel('Moodiness')
plt.title('Bar Chart of WHAT-IF Q1, Q2, Q3 Outcomes')
# Show the plot
plt.show()