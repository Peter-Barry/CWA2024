import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = 'flucheck.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Total each of the 4 columns
total_values = df.sum()

# Plot the Pie Chart
plt.pie(total_values, labels=total_values.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
plt.title('Flu Vaccine Status (Pie Chart)')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Show the Pie Chart
plt.show()
