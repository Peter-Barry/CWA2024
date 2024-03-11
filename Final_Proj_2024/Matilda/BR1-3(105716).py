#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep

#function to give a remark on my mood based on avg_mood value
def interpret_mood(avg_mood):
    if avg_mood >= 9:
        return "excellent, I'm feeling amazing today."
    elif avg_mood <  5:
        return "Okay, hopefully better soon."
    elif 5 <= avg_mood < 9:
        return "improving thanks."
    else:
        return "questionable, not enough info. \n"
    

#Take them in as integers, as all inputs default to strings
physical_wellbeing = int(input("On a scale of 1-10 from tired to energised, how much energy do you have? "))
study_wellbeing = int(input("On a scale of 1-10 from unprepared to prepared, how ready are you for your exams? "))
financial_wellbeing = int(input("On a scale of 1-10 from poor to rich, how financially supported are you? "))
avg_mood = round(mean([physical_wellbeing,study_wellbeing,financial_wellbeing]),2)
mood_remark = interpret_mood(avg_mood)
print("My Average mood today is",mood_remark, "Average mood is", avg_mood)


df = pd.read_csv('drankornot.csv')
#print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
temperature_min = df['temperature'].min()
temperature_max = df['temperature'].max()
temperature_mean = df['temperature'].mean()
print ("Minimum temperature is", temperature_min, "Maximum temperature is", temperature_max, "Mean temperature is",temperature_mean)

#Validation of my data for BR2 - changing if needed before it gets added to my results file
if not isinstance(temperature_min, float):
    temperature_min = float(temperature_min)
if not isinstance(temperature_max, float):
    temperature_max = float(temperature_max)
if not isinstance(temperature_mean, float):
    temperature_mean = float(temperature_mean)

f = open("BR1-3_results.csv", "a", newline='')
csver = csv.writer(f)

#csver.writerow (["Temperature_min", "Temperature_max", "Temperature_mean", "Average mood"])
csver.writerow([temperature_min, temperature_max, temperature_mean, avg_mood])

print("The following output results will be added to my 'BR1-3_results.csv' file")
print([temperature_min, temperature_max, temperature_mean, avg_mood])
print("")
f.close()

# Preview of results spreadsheet using pandas extension
df2 = pd.read_csv('BR1-3_results.csv')
print(df2)


