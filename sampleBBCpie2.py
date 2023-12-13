import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = 'sampleBBCdata.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Process columns btnA, btnB, and btnA&B
btn_columns = ['btnA', 'btnB', 'btnA&B']

# Calculate total of value 1 and total of value 2 for each column
totals = [df[column].eq(1).sum() for column in btn_columns]

# Data to plot
labels = btn_columns
sizes = totals
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0.1, 0.1)  # explode 1st slice for each column

# Plot the Pie Chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Total of Value 1 for btnA, btnB, and btnA&B')
plt.show()
