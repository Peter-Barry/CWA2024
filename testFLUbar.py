import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = 'flucheck.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Total each of the 4 columns
total_values = df.sum()

# Plot the Bar Chart
plt.bar(total_values.index, total_values, color=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
plt.title('Flu Vaccine Status (Bar Chart)')
plt.xlabel('Vaccine Status')
plt.ylabel('Total Count')

# Show the Bar Chart
plt.show()
