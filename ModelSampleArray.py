import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
data = {
    'Timestamp': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
    'HeartRate': [70, 72, 65, 68],
    'Temperature': [98.6, 98.4, 98.7, 98.5],
    'Age': [25, 26, 27, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'SoundLevel': [30, 32, 28, 31]
}

df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

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
what_if_gender('Female')
what_if_heart_rate(67)
