import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is in a CSV file named 'mood_data.csv'
file_path = 'CWA_your_dataset_copy2.csv'
df = pd.read_csv(file_path)
print(df.columns)


# Plotting the line chart
plt.figure(figsize=(10, 6))

# Plot each column as a line
plt.plot(df['Hours_study'], label='Hours of Study', marker='o')
plt.plot(df['Hours_sleep'], label='Hours of Sleep', marker='o')
plt.plot(df['Hours_exercise'], label='Hours of Exercise', marker='o')
plt.plot(df['Mood_Score'], label='Mood Score', marker='o')

# Adding labels and title
plt.xlabel('Days')
plt.ylabel('Values')
plt.title('Mood Data Over Days')

# Adding legend
plt.legend()

# Show the plot
plt.show()
