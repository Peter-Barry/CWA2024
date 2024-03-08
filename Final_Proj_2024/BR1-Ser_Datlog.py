#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
#Function to remove all the alpha chars from the light MicroBit data
def remove_alpha(input_str):
    # Create a new string containing only digits
    result_str = ''.join(char for char in input_str if char.isdigit())
    return result_str


# TAKE IN LIGHT DATA FROM MICROBIT PROCESS REQUIRING THEM MICROBIT TO BE RUNNING
# blank list for light data
lightList = []
ser = serial.Serial()
ser.baudrate = 115200
#what is the bloody port number, find it on windows machine by checking device manager
ser.port = "COM3"
ser.open()
for x in range(10):
        # First take in all the data and assign it to this variable
        microbitdata = str(ser.readline())
        print("here",microbitdata)
        light_data = microbitdata[2:]

        """
        # Get second bit onwards, call that signal_in
        light_data = microbitdata[2:]

        # Remove any spaces, data validation!
        light_data = light_data.replace(" ","")

        # Remove any apostrophies, data validation!
        light_data = light_data.replace("'","")

        # Replace this with nothing (remove it), data validation!
        light_data = light_data.replace("\\r\\n","")
        #remove alphas
        """
        light_data = remove_alpha(light_data)
        print("removed alphas", light_data)
        
        #Validation checking to ensure the data is integer and changing to float
        light_data = float(light_data)
        
        # Print it to see if any of that rubbish above actually worked
        #print(type(light_data))
        #VALIDATION
        #add data to list! But only if its a float, so null types which are common on Microbits will never get added to the data
        #if type(light_data) == float:
        lightList.append(light_data)

print("LightDataaaa =  ", lightList)
#The three parameters for project
#maxLight = round(max(lightList),2)
#minLight = round(min(lightList),2)
#meanLight = round(mean(lightList),2)
#print("Max Light List is ",maxLight,"Min Light List is ",minLight,"Mean Light List is ",meanLight)

"""

#write the combined avg light data and average mood to a CSV file
f = open("BR1-3_results-serial.csv", "a", newline='')
csver = csv.writer(f)
# Should I write the column headings here? They will repeat down the sheet
# for each run of the code, remove this line of code, create the data IE several
# columns and then manually create the column headings in prep for AReqs Pandas
#csver.writerow(["light_min", "light_max", "light_mean", "avg_mood"])
csver.writerow([minLight, maxLight, meanLight, avg_mood])

print("I have added the following data to the data file BR1-3_results.csv")
print([minLight, maxLight, meanLight, avg_mood])
print("")
f.close()

# Preview what is now in the spreadsheet using pandas
df = pd.read_csv('BR1-3_results.csv')
print(df)
#Its necessary to run this code several times as it creates a single ROW of data in the O/P
#file each run. Only after running several times will you get several rows of DATA for the
#AR1-3 programs
#It is also necessary to open the data and add the column labels before running into
#AR1-3 progs
"""