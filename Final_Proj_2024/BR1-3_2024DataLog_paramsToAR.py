#import statements here
import pandas as pd
from statistics import mean
import csv

#function to give a remark on my mood based on avg_mood value
def interpret_mood(avg_mood):
    if avg_mood >= 9:
        return "Excellent mood today, thank god"
    elif avg_mood <  5:
        return "Middlin today, thanks for asking"
    elif 5 <= avg_mood < 9:
        return "Improving thanks."
    else:
        return "Not really sure, not enough info \n"

#Take in 3 wellness indicators
#Take them in as integers, as all inputs default to strings
intellectual_wellness = int(input("On a scale of 1-10 from poorly to ready, how prepared for exams are you?"))
physical_wellness = int(input("On a scale of 1-10 from tired to energetic, how much energy do you have?"))
social_wellness = int(input("On a scale of 1-10 from crappy friend relations to happy/clappy friend relations to ?"))
avg_mood = round(mean([intellectual_wellness,physical_wellness,social_wellness]),2)
mood_remark = interpret_mood(avg_mood)
print("My Average mood today is ",mood_remark, " ", avg_mood)

#reads a csv file created by a microbit program "BR1-3_2024_light"
#the data is light recording, can be changed to sound , accelleration, temp
df = pd.read_csv('MicroBitLightData.csv')
print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
light_min = df['Light'].min()
light_max = df['Light'].max()
light_mean = df['Light'].mean()
print (light_min,light_max,light_mean, avg_mood)
#DATA VALIDATION BR2, validating and if necessary modifying the VARIABLE data before writing the Data to output file
if not isinstance(light_min, float):
    light_min = float(light_min)
if not isinstance(light_mean, float):
    light_mean = float(light_mean)
if not isinstance(light_max, float):
    light_max = float(light_max)

#write the combined avg light data and average mood to a CSV file
f = open("BR1-3_results.csv", "a", newline='')
csver = csv.writer(f)
# Should I write the column headings here? They will repeat down the sheet
# for each run of the code, remove this line of code, create the data IE several
# columns and then manually create the column headings in prep for AReqs Pandas
#csver.writerow(["light_min", "light_max", "light_mean", "avg_mood"])
csver.writerow([light_min, light_max, light_mean, avg_mood])

print("I have added the following data to the data file BR1-3_results.csv")
print([light_min, light_max, light_mean, avg_mood])
print("")
f.close()

# Preview what is now in the spreadsheet using pandas
df2 = pd.read_csv('BR1-3_results.csv')
print(df2)

