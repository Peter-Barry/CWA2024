import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Training the model

# Load your dataset
data = pd.read_csv('your_dataset_copy.csv')
# Define your independent variables (features) and dependent variable (target)
X = data[['Hours_study', 'Hours_sleep', 'Hours_exercise']]
Y = data['Mood_Score']
# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)
# Predicting mood scores for the test set
Y_pred = model.predict(X_test)

mse = mean_squared_error(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")

# I had no idea what MEAN SQUARED meant so this scale might be helpful to you
def interpret_mse(mse):
    if mse < 10:
        return "Excellent model accuracy. This is the SHIZ."
    elif mse < 20:
        return "Good model accuracy. A fine auld model."
    elif mse < 30:
        return "Average model accuracy. That'll do pig."
    elif mse < 40:
        return "Below average model accuracy. Don't bet your house on this being true."
    else:
        return "Poor model accuracy! Get better data or try another fit like polyfit. This shirt ain't linear. \n"

mse_remark = interpret_mse(mse)
print(mse_remark)

def predict_mood(hours_of_study, hours_sleep, hours_exercise):
    df = pd.DataFrame([[hours_of_study, hours_sleep, hours_exercise]],
                      columns=['Hours_study', 'Hours_sleep', 'Hours_exercise'])
    return model.predict(df)[0]

study = int(input("Enter study hours. Can be any integer from 0-8 "))
sleep = float(input("Enter sleep hours. Can be anything from 1-12 "))
exercise = float(input("Enter exercise hours. Can be anything from 1-4 "))

predicted_mood = predict_mood(study, sleep, exercise)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)

