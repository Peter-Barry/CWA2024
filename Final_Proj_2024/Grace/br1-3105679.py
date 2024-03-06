#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
#function to give a remark on my wellbeing based on avg_wellbeing value
def interpret_wellbeing(avg_wellbeing):
    if avg_wellbeing>= 9:
        return "Excellent mood today, thank god"
    elif avg_wellbeing <  5:
        return "Not the best today, thanks for asking"
    elif 5 <= avg_wellbeing < 9:
        return "Improving thanks."
    else:
        return "Not really sure, not enough info \n"
    #Take them in as integers, as all inputs default to strings
social_wellbeing = int(input("On a scale of 1-10 from good to bad, how is your social-wellbeing?"))
mental_wellbeing = int(input("On a scale of 1-10 from happy to depressed, how are you feeling mentally?"))
physical_wellbeing = int(input("On a scale of 1-10 from energetic to lazy , how much energy do you have"))
avg_wellbeing = round(mean([social_wellbeing,mental_wellbeing,physical_wellbeing]),2)
wellbeing_remark = interpret_wellbeing(avg_wellbeing)
print("My Average wellbeing today is ",wellbeing_remark, " ", avg_wellbeing)

#reads a csv file created by a microbit program "BR1-3_2024_light"
df = pd.read_csv('microbitdata.csv')
print(df)

light_min = df['Light'].min()
light_max = df['Light'].max()
light_mean = df['Light'].mean()
print (light_min,light_max,light_mean, avg_wellbeing)
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

csver.writerow([light_min, light_max, light_mean, avg_wellbeing])

print("I have added the following data to the data file BR1-3_results.csv")
print([light_min, light_max, light_mean, avg_wellbeing])
print("")

f.close()

df2 = pd.read_csv('BR1-3_results.csv')
print(df2)
f.close()
    
