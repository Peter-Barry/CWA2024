

#Import statements
import pandas as pd  # for use with analysing data
import csv           # for use with any CSV file handlin
from statistics import mean # for use with calculations on any data or variables

#This functions asks user to enter on a scale how their wellness is on 3 indicators and calculates an averqge  mood
def take_wellness_indicators():
    intellectual_wellness = int(input("On a scale of 1-10 from poorly to ready, how prepared for exams are you?"))
    physical_wellness = int(input("On a scale of 1-10 from tired to energetic, how much energy do you have?"))
    social_wellness = int(input("On a scale of 1-10 from crappy friend relations to happy/clappy friend relations to ?"))
    avg_mood = round(mean([intellectual_wellness, physical_wellness, social_wellness]), 2)
    print("My Average mood today is ", avg_mood)
    return avg_mood
#This function reads my microbit light sensed data
def read_light_data():
    df = pd.read_csv('MicroBitLightData.csv')
    return df
# This function valuidates the data from the microbit to ensure it can be processed correctly
def validate_data(light_min, light_max, light_mean):
    if not isinstance(light_min, float):
        light_min = float(light_min)
    if not isinstance(light_mean, float):
        light_mean = float(light_mean)
    if not isinstance(light_max, float):
        light_max = float(light_max)
    return light_min, light_max, light_mean
# this function writes my output data from BR1-3 
def write_to_csv(light_min, light_max, light_mean, avg_mood):
    with open("BR1-3_results.csv", "a", newline='') as f:
        csver = csv.writer(f)
        csver.writerow([light_min, light_max, light_mean, avg_mood])
        print("data out to the data file output csv file")
        print([light_min, light_max, light_mean, avg_mood])
        print("")



avg_mood = take_wellness_indicators() #Get an average mood
df = read_light_data()                # Read the microbit data
light_min = df['Light'].min()         # Calc Minimum value from this column of data
light_max = df['Light'].max()         # Calc Maximum value from this column of data
light_mean = df['Light'].mean()       # Calc Mean value from this column of data
# Here we valiudate the data before writing it to output file
light_min, light_max, light_mean = validate_data(light_min, light_max, light_mean)
write_to_csv(light_min, light_max, light_mean, avg_mood)
#take a look at the data to see how it looks
df = pd.read_csv('BR1-3_results.csv')
print(df)



