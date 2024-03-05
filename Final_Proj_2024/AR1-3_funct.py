import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def train_model(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    my_model = LinearRegression()
    my_model.fit(X_train, Y_train)
    return my_model, X_test

def predict_mood(model, hours_of_sunlight, average_sunlight, peak_sunlight):
    df = pd.DataFrame([[hours_of_sunlight, average_sunlight, peak_sunlight]],
                      columns=['Hours_Light', 'Intensity_Light', 'Peak_Light'])
    return round(model.predict(df)[0], 2)

def get_user_input():
    hours = int(input("Enter sunlight hours. Can be any integer from 0-24: "))
    sun = float(input("Enter average sunlight intensity. Can be anything from 1-800: "))
    peak = float(input("Enter peak sunlight level. Can be anything from 1-800: "))
    return hours, sun, peak

def display_mood_prediction(mood):
    print("\nThe Predicted Mood Score for the values entered is", mood)

def display_what_if_questions(mood_if_lowSun, mood_if_NormalSun, mood_if_HighSun):
    print("-----------------------------------------------------------")
    print("WHAT-IF QUESTION 1")
    print("Let's test what the mood will be if the sunlight is very low")
    print("\nThe low sun score mood is", mood_if_lowSun)

    print("-----------------------------------------------------------")
    print("WHAT-IF QUESTION 2")
    print("Let's test what the mood will be if the sunlight is very high")
    print("\nThe higher sun score mood is", mood_if_HighSun)

    print("-----------------------------------------------------------")
    print("WHAT-IF QUESTION 3")
    print("Let's test mood if medium sunlight")
    print("\nThe middle sunlight Score mood is", mood_if_NormalSun)

def plot_bar_chart(variable_names, values):
    plt.bar(variable_names, values)
    plt.xlabel('Amount of Sun')
    plt.ylabel('Mood')
    plt.title('Bar Chart of all 3 WHAT-IFs Predictions')
    plt.show()

def main():
    data = load_data('AR1-3_Input-Copy.csv')
    X = data[['Hours_Light', 'Intensity_Light', 'Peak_Light']]
    Y = data['Mood_Score']
    my_model, X_test = train_model(X, Y)

    hours, sun, peak = get_user_input()
    predicted_mood = predict_mood(my_model, hours, sun, peak)
    display_mood_prediction(predicted_mood)

    mood_if_lowSun = predict_mood(my_model, 2, 100, 200)
    mood_if_NormalSun = predict_mood(my_model, 6, 300, 300)
    mood_if_HighSun = predict_mood(my_model, 15, 600, 800)

    display_what_if_questions(mood_if_lowSun, mood_if_NormalSun, mood_if_HighSun)

    variable_names = ['Mood if lowSun', 'Mood if NormalSun', 'Mood if HighSun']
    values = [mood_if_lowSun, mood_if_NormalSun, mood_if_HighSun]
    plot_bar_chart(variable_names, values)

main()
