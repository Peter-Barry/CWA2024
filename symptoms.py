# Name : Your Name
# Program Name : LO 3.1 Symptoms
# Date : Today’s date
# Description of Program
# To take in data from the screen and populate two lists declared inside the program
#
# You always declare lists at the top of the program
# You MUST put data inside any declared lists IE 1,2,3 or "a","b","c" etc
#
# Declare the lists
import matplotlib.pyplot as plt

symptoms = [1,2,3]
students = ["a","b","c"]
# take in data from the screen
symptoms[0] = input("enter a first symptom ")
students[0] = input("enter how many students had the first symptom ")
symptoms[1] = input("enter a second symptom ")
students[1] = input("enter how many students had the second symptom ")
symptoms[2] = input("enter a third symptom ")
students[2] = input("enter how many students had the third symptom ")
# Data to plot
labels = symptoms[0], symptoms[1], symptoms[2]
sizes = [students[0], students[1], students[2]]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0.1, 0.1)  # explode 1st slice
# Plot the Pie Chart (Do not change any code below)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
#plt.axis('equal')
plt.show()
