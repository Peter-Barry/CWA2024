import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = 'sampleBBCdata.csv'  # Replace with the actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Extract columns for pie charts
btn_columns = ['btnA', 'btnB', 'btnA&B']
logo_column = 'LOGO'
sound_temp_light_columns = ['Sound', 'Temp', 'Light']

# Create pie charts
def create_pie_chart(data, title):
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral'])
    plt.title(title)
    plt.show()

# Pie chart for btnA, btnB, btnA&B
for btn_column in btn_columns:
    btn_data = df[btn_column].value_counts()
    create_pie_chart(btn_data, f'{btn_column} Pie Chart')

# Pie chart for LOGO
logo_data = df[logo_column].value_counts()
create_pie_chart(logo_data, f'{logo_column} Pie Chart')

# Pie chart for Sound, Temp, Light
for stl_column in sound_temp_light_columns:
    stl_data = df[stl_column].value_counts()
    create_pie_chart(stl_data, f'{stl_column} Pie Chart')
