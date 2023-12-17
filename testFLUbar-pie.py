import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = 'flucheck.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Total each of the 4 columns
total_values = df.sum()

# Create a figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot the Pie Chart
axs[0].pie(total_values, labels=total_values.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
axs[0].set_title('Flu Vaccine Status (Pie Chart)')

# Plot the Bar Chart
axs[1].bar(total_values.index, total_values, color=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
axs[1].set_title('Flu Vaccine Status (Bar Chart)')
axs[1].set_xlabel('Vaccine Status')
axs[1].set_ylabel('Total Count')

# Adjust layout for better visualization
plt.tight_layout()

# Show both charts
plt.show()
