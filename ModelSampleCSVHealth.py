import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file
df = pd.read_csv('HealthSampleData.csv')

# Convert 'Timestamp' column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Visualization: Progress over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Timestamp', y='HeartRate', data=df, label='Heart Rate')
sns.lineplot(x='Timestamp', y='Temperature', data=df, label='Temperature')
plt.title('Wellbeing Progress Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()

# Answering "what if" questions
def what_if_gender(gender):
    subset = df[df['Gender'] == gender]
    print(f'Average Heart Rate for {gender}: {subset["HeartRate"].mean()} BPM')

def what_if_heart_rate(threshold):
    above_threshold = df[df['HeartRate'] > threshold]
    print(f'Number of instances with heart rate above {threshold} BPM: {len(above_threshold)}')

# "What if" questions
user_gender = input("Enter your gender (Male/Female): ")
what_if_gender(user_gender)

user_heart_rate_threshold = float(input("Enter your desired heart rate threshold: "))
what_if_heart_rate(user_heart_rate_threshold)
