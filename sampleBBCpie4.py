import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = 'sampleBBCdata.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Display the DataFrame for verification
print(df)

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
plt.pie(sizes_stl, explode=explode_stl, labels=labels_stl, colors=colors_stl,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Total for Sound, Temp, and Light columns')

# Show the plot
plt.show()
