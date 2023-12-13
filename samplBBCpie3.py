import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = 'sampleBBCdata.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Process columns btnA, btnB, and btnA&B
btn_columns = ['btnA', 'btnB', 'btnA&B']

# Calculate total of value 1 and total of value 0 for each column
totals_btn = [df[column].eq(1).sum() for column in btn_columns]

# Data to plot for btn columns
labels_btn = btn_columns
sizes_btn = totals_btn
colors_btn = ['gold', 'yellowgreen', 'lightcoral']
explode_btn = (0.1, 0.1, 0.1)  # explode 1st slice for each column

# Plot the Pie Chart for btn columns
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(sizes_btn, explode=explode_btn, labels=labels_btn, colors=colors_btn,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Total of Value 1 for btnA, btnB, and btnA&B')
"""
# Process columns Sound, Temp, and Light
stl_columns = ['Sound', 'Temp', 'Light']

# Calculate total for each column
totals_stl = [df[column].sum() for column in stl_columns]

# Data to plot for Sound, Temp, and Light columns
labels_stl = stl_columns
sizes_stl = totals_stl
colors_stl = ['skyblue', 'lightgreen', 'lightcoral']
explode_stl = (0.1, 0.1, 0.1)  # explode 1st slice for each column

# Plot the Pie Chart for Sound, Temp, and Light columns
plt.subplot(1, 2, 2)
plt.pie(sizes_stl, explode=explode_stl, labels=labels_stl, colors=colors_stl,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Total for Sound, Temp, and Light columns')
"""
# Show the plots
plt.tight_layout()
plt.show()
