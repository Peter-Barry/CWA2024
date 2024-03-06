#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
import matplotlib.pyplot as plt

#Take them in as integers, as all inputs default to strings
financial_situation = int(input("On a scale of 1-10 from insufficient to a sufficient amount of money, are you in a stable financial position? "))
physical_wellness = int(input("On a scale of 1-10 from no pain to painful, how is the pain in your head? "))
social_wellbeing = int(input("On a scale of 1-10 from good family relationships to poor family relationships, how is your familial relationships? "))
avg_mood = round(mean([financial_situation,physical_wellness,social_wellbeing]),2)

print("My Average mood today is ", avg_mood)

df = pd.read_csv('MicroBitSound.csv')
print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
sound_min = df['sound level'].min()
sound_max = df['sound level'].max()
sound_mean = df['sound level'].mean()
print (sound_min,sound_max,sound_mean, avg_mood)
if not isinstance(sound_min, float):
    sound_min = float(sound_min)
if not isinstance(sound_max, float):
    sound_max = float(sound_max)
if not isinstance(sound_mean, float):
    sound_mean = float(sound_mean)

f = open("BR1-3_results.csv", "a", newline='')
csver = csv.writer(f)

csver.writerow([sound_min, sound_max, sound_mean, avg_mood])
print("")
f.close()

"""
# Preview what is now in the spreadsheet using pandas
df = pd.read_csv('BR1-3_results.csv')
print(df)

# Specify the file path
file_path = 'BR1-3_results.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Total each of the 4 columns
total_values = df.sum()

# Plot the Bar Chart
variable_names = ['Min sound', 'Max sound','Mean sound', 'Average mood']
values = [sound_min, sound_max ,sound_mean, avg_mood ]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Level of sound')
plt.ylabel('Amount')
plt.title('Bar Chart of all 3 WHAT-IFs Predictions')

# Show the plot
plt.show()



plt.bar(total_values.index, total_values, color=['blue', 'green', 'red', 'pink'])
plt.title('Sound (Bar Chart)')
plt.xlabel('measure of sound')
plt.ylabel('Total Count')

# Show the Bar Chart
plt.show()
"""