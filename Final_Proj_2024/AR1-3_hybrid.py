#Import Statements
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Getting user input to use in the model
def get_user_input():
    hours = int(input("Enter sunlight hours. Can be any integer from 0-24: "))
    sun = float(input("Enter average sunlight intensity. Can be anything from 1-800: "))
    peak = float(input("Enter peak sunlight level. Can be anything from 1-800: "))
    return hours, sun, peak
# using the model to get a prediction using my data from the screen or what-if Qs
def predict_mood(hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity):
    df = pd.DataFrame([[hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity]],
                      columns=['Hours_Light', 'Intensity_Light', 'Peak_Light'])
    return my_model.predict(df)[0]
# Function to output the result of the whatif questions 1-3

# Training the model
# first Load your dataset
data = pd.read_csv('AR1-3_Input-Copy.csv') # This dataset is a copy of the output from BR1-3, copied so as to create a backup of BR1-3 data

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


print("Linear Regression to the Model Complete!")

# Making a prediction using the model
# Let the user enter their own 3 parameters
# Note 2 different datatypes
print("")
print("USER CHOOSES 3 LIGHT LEVELS MODE")
hours, sun, peak = get_user_input()
predicted_mood = round(predict_mood(hours, sun, peak),2)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)

#___________________What If Questions AR2 _________
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 1")
print("Let's test what the mood will be if the sunlight is very low")
mood_if_lowSun = round(predict_mood(2, 100, 200),2)
print("\n The low sun score mood is", mood_if_lowSun)
print("")
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 3")
print("Let's test mood if medium sunlight")
mood_if_NormalSun = round(predict_mood(6, 300, 300),2)
print("\n The middle sunlight Score mood is", mood_if_NormalSun)
print("")
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 2")
print("Let's test what the mood will be if the sunlight is very high")
mood_if_HighSun = round(predict_mood(15, 600, 800),2)
print("\n The higher sun score mood is", mood_if_HighSun)

# Data: names of the variables and their values for the Bar Chart    AR3
#------------------------------------
# AR3 Users can view data in a graphical format which displays information such as their progress
#using the system or the results of a ‘what if’ scenario.

# Data: names of the variables and their values for the chart
variable_names = ['Mood if lowSun', 'Mood if NormalSun','Mood if HighSun']
values = [mood_if_lowSun, mood_if_NormalSun,mood_if_HighSun]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Ammount of Sun')
plt.ylabel('Mood')
plt.title('Bar Chart of all 3 WHAT-IFs Predictions')

# Show the plot
plt.show()







