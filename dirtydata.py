

import pandas as pd
import numpy as np
import plotly.express as px



# Load the dataset
input_file = 'dirtydata.csv'
data = pd.read_csv(input_file)

# Inspect the dataset
print(data.head())
print(data.info())

# Clean the dataset: Replace '*' and '$' with an empty string
data = data.replace({'\%': ''}, regex=True)

# Drop unnecessary columns
if 'Name' in data.columns:
    data = data.drop('Name', axis=1)
if 'Extracurricular_Activities' in data.columns:
    data = data.drop('Extracurricular_Activities', axis=1)



# Output the cleaned data to a new CSV file
output_file = 'cleaned.csv'
data.to_csv(output_file, index=False)



#Define non-numeric cols:
non_numeric_cols = ['Gender','Department','Internet_Access_at_Home','Grade']

#Create a dictionary called stats_dictionary
stats_dictionary = {}

for col in data.columns:
    if col not in non_numeric_cols:
        stats_data = pd.to_numeric(data[col], errors='coerce')
        
        stats_dictionary[col] = {
            'Mean'   : stats_data.mean(),
            'Median' : stats_data.median(),
            'Mode'   : stats_data.mode().iloc[0] if not stats_data.mode().empty else np.nan,
            'Range'  : stats_data.max() - stats_data.min()
            }
print(stats_dictionary)
        



# Load the dataset 
file_path = 'cleaned.csv'  
df = pd.read_csv(file_path)

# Create the pie chart for Grade Distribution
fig = px.pie(
    df, 
    names='Grade', 
    title='Grade Distribution Among Students', 
    hole=0,  
    color_discrete_sequence=px.colors.sequential.RdBu
)

# Show the plot
fig.show()



df = pd.DataFrame(data)

# Create bubble scatter plot
fig = px.scatter(
    df, x="Study Hours", y="Final Score", 
    size="Attendance", color="Final Score",
    title="Study Hours vs. Final Score",
    labels={"Study Hours": "Hours Studied per Week", "Final Score": "Final Exam Score"},
    hover_data=["Attendance"]
)

fig.show()

#List data needed for scatter plot
data = {
    "Study Hours": [6.2,19,20.7,24.8,15.4,21.3,27,3,8,9.6,13.2,21.3,18.1,22.8,5.8,25.3,29.7,6.2,17.4,25.3,16.9,19.8,28,18.5,10.9,23.5,14.4,12.1,11.2]
    "Final Score" : [57.82,45.8,93.68,80.63,78.89,89.07,73.96,90.87,98.47,8

