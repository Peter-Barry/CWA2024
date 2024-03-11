#import statements here
import pandas as pd
from statistics import mean
import csv
import matplotlib.pyplot as plt

#Calculate the min,max,mean from the light data off the MicroBit
def calculate_light_statistics(df, avg_mood):
    light_min = df['Light'].min()
    light_max = df['Light'].max()
    light_mean = df['Light'].mean()
    
    # Print the calculated statistics and the average mood
    print("Minimum Light:", light_min, " ","Maximum Light:", light_max, " ", "Mean Light:", light_mean, " ","Average Mood:", avg_mood)
    return light_min, light_max, light_mean, avg_mood


#function to give score on overall health
def interpret_health(avg_health):
    if avg_health >= 9:
        return "Excellent health today, well done"
    elif avg_health <  5:
        return "Average health today"
    elif 5 <= avg_mood < 9:
        return "Need to get healthier."
    else:
        return "Not really sure, not enough info \n"

#Take variables in as integers or floats
glasses_water = int(input("How many glasses of water have you had today? "))
physical_wellness = int(input("On a scale of 1-10 from tired to energetic, how much energy do you have?"))
heart_rate = float(input("What was your heart rate at rest before your walk?"))

if 0<= glasses_water <5:
    print("You need to drink more water \n")
    hydration_level = glasses_water
elif 5<= glasses_water <= 9:
    print("Well done, you have achieved the recommended daily water intake \n")
    hydration_level = glasses_water
elif 9 < glasses_water <= 13:
    print("You may be drinking too much \n")
    hydration_level = 10
elif glasses_water > 13:
    print("Please be aware that drinking too much water can be detrimental for your health \n")
    hydration_level = 2
else:
    print("Sorry, you have entered an invalid value \n")
    hydration_level = -1
    
    print("Your hydration score is: ", hydration_level)
#calculate an average mood basd on the 3 wellness indicators taken in from screen    
avg_mood = round(mean([glasses_water,physical_wellness,heart_rate]),2)
print("My Average mood today is ",avg_mood)
#read in the light data from the microbit system
df = pd.read_csv('LightData-105616.csv')
print(df)
#Call function to Calculate/return the min,max,mean 
light_min, light_max, light_mean, avg_mood = calculate_light_statistics(df, avg_mood)

#VALIDATION OF DATA BR2
if not isinstance(light_min, float):
    light_min = float(light_min)
if not isinstance(light_max, float):
    light_max = float(light_max)
if not isinstance(light_mean, float):
    light_mean = float(light_mean)

f = open("BR1-3_results-105616.csv", "a", newline='')
csver = csv.writer(f)

csver.writerow([light_min, light_max, light_mean, avg_mood])
f.close()

# Preview what is now in the spreadsheet using pandas
df2 = pd.read_csv('BR1-3_results-105616.csv')
print(df2)

# names of the variables and their values for the chart
chart_variable_names = ['Mood if lowSun', 'Mood if NormalSun','Mood if HighSun','Avg Mood']
chart_values = [light_min, light_mean,light_max,avg_mood]

# Creating the bar chart
plt.bar(chart_variable_names, chart_values)

# Adding axis labels and chart title
plt.xlabel('Ammount of Sun')
plt.ylabel('Mood')
plt.title('Bar Chart of Light Values and Mood')

# Show the plot
plt.show()
