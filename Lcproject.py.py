
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Load the dataset
input_file = 'dirtydata.csv'
data = pd.read_csv(input_file)

# Inspect the dataset
print(data.head())
print(data.info())

# Clean the dataset: Replace '*' and '$' with an empty string
data = data.replace({'\*': ''}, regex=True)
data = data.replace({'\$': ''}, regex=True)

# Drop unnecessary columns
if 'Rank' in data.columns:
    data = data.drop('Rank', axis=1)
if 'Year' in data.columns:
    data = data.drop('Year', axis=1)
if 'Genres' in data.columns:
    data = data.drop('Genres', axis=1)


# Output the cleaned data to a new CSV file
output_file = 'cleaned.csv'
data.to_csv(output_file, index=False)





non_numeric_cols = ['Movie', 'Country']

# Create a dictionary to store statistics
stats_dictionary = {}






# Data
categories = ['$Worldwide', '$Domestic', 'Domestic %']
statistics = ['Mean', 'Median', 'Mode', 'Range']
values = [
    [2.646157e+08, 1.329046e+08, 5.099655e+01],  # Mean
    [237202299.0, 124115725.0, 50.3],            # Median
    [149270999.0, 66957026.0, 39.4],             # Mode
    [397117109.0, 193788594.0, 43.3],            # Range
]

# Transpose data for plotting
values = np.array(values).T

# Plot
x = np.arange(len(categories))  # Labels positions
width = 0.2  # Bar width

plt.figure(figsize=(10, 6))
for i, stat in enumerate(statistics):
    plt.bar(x + i * width, values[:, i], width, label=stat)

# Customization
plt.xticks(x + width, categories)
plt.xlabel('Categories')
plt.ylabel('Values(100s millions)')
plt.title('Comparison of Mean, Median, Mode, and Range')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)




# Show plot
plt.tight_layout()
plt.show()

