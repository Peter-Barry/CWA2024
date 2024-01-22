
import serial
from time import sleep
from statistics import mean

def remove_alpha(input_str):
    # Create a new string containing only digits
    result_str = ''.join(char for char in input_str if char.isdigit())
    return result_str

# blank list for light data
lightList = []
ser = serial.Serial()
ser.baudrate = 115200
#what is the bloody port number, find it on windows machine by checking device manager
ser.port = "COM3"

ser.open()

# Start the loop to read serial data! Change the number up from 4 to whatever you want
for x in range(4):
        # First take in all the data and assign it to this variable
        microbitdata = str(ser.readline())
        # Get second bit onwards, call that signal_in
        light_data = microbitdata[2:]

        # Remove any spaces, data validation!
        light_data = light_data.replace(" ","")

        # Remove any apostrophies, data validation!
        light_data = light_data.replace("'","")

        # Replace this with nothing (remove it), data validation!
        light_data = light_data.replace("\\r\\n","")
        #remove alphas
        light_data = remove_alpha(light_data)
        print("removed alphas", light_data)
        
        #Validation checking to ensure the data is integer and changing to float
        light_data = float(light_data)
        
        # Print it to see if any of that rubbish above actually worked
        #print(type(light_data))
        #VALIDATION
        #add data to list! But only if its a float, so null types which are common on Microbits will never get added to the data
        if type(light_data) == float:
            lightList.append(light_data)

print("LightData = ", lightList)
#The three parameters for project
maxLight = round(max(lightList),2)
minLight = round(min(lightList),2)
meanLight = round(mean(lightList),2)
print("Max Light List is ",maxLight,"Min Light List is ",minLight,"Mean Light List is ",meanLight)
