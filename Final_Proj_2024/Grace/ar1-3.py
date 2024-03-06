import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Prediction function to predict using 3 independent variables and one dependent variable. 
def predict_wellbeing(hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity):
    df = pd.DataFrame([[hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity]],
                      columns=['Hours_Light', 'Intensity_Light', 'Peak_Light'])
    return my_model.predict(df)[0]



data = pd.read_csv('AR1-3-105679.csv') # This dataset is a copy of the output from BR1-3, copied so as to create a backup of BR1-3 data

# Defining my independent variables and dependent variable
elements = data[['Hours_Light', 'Intensity_Light', 'Peak_Light']]

wellbeing = data['Mood_Score']

# Splitting the dataset into training and test sets
elements_train, elements_test, wellbeing_train, wellbeing_test = train_test_split(elements, wellbeing, test_size=0.2, random_state=0)

# Creating the Linear Regression model
my_model = LinearRegression()

# Fitting the model with the training data
my_model.fit(elements_train, wellbeing_train)

# Predicting mood scores for the test set
wellbeing_pred = my_model.predict(elements_test)


print("My Multiple Linear Regression Model is now Complete!")

# Making a prediction using the model
# Let the user enter their own 3 parameters
# Note 2 different datatypes
print("")
print("USER CHOOSES 3 LIGHT LEVELS MODE")
hours = int(input("Enter sunlight hours. Can be any integer from 0-24 "))
sun = float(input("Enter average sunlight today. Can be anything from 1-800 "))
peak = float(input("Enter peak sunlight level. Can be anything from 1-800 "))

predicted_wellbeing = predict_wellbeing(hours, sun, peak)  # Example values
print("\n The Predicted wellbeing Score for the values entered is", predicted_wellbeing)

#___________________What If Questions AR2 _________
# WHAT-IF Q1
# What is will your mood be with low values given to the 3 params?

print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 1")
print("Let's test what the mood will be if the sunlight is very low")

# Low values for all 3 parameters
hours_of_sunlight = 2
average_sunlight = 100
peak_sunlight = 200

wellbeing_if_lowSun = round(predict_wellbeing(hours_of_sunlight, average_sunlight, peak_sunlight),2)  # Example values
print("\n The low sun score mood is", wellbeing_if_lowSun)
