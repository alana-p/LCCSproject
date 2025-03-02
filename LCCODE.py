
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
        


import pandas as pd
import plotly.express as px

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











# Load the dataset (replace with your actual file path if needed)
file_path = 'cleaned.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Calculate average final scores per department
avg_scores = df.groupby('Department')['Final_Score'].mean().reset_index()

# Create the bar chart
fig = px.bar(
    avg_scores, 
    x='Department', 
    y='Final_Score', 
    title='Average Final Scores by Department', 
    color='Final_Score',
    text=round(avg_scores['Final_Score'], 2),  # Display values on bars
    color_continuous_scale='Blues'
)

# Customize layout
fig.update_layout(
    xaxis_title='Department',
    yaxis_title='Average Final Score',
    template='plotly_dark'
)

# Show the plot
fig.show()



import pandas as pd
import plotly.express as px

# Load the dataset (replace with your actual file path if needed)
file_path = 'cleaned.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Create the scatter plot
fig = px.scatter(
    df, 
    x='Study_Hours_per_Week', 
    y='Final_Score', 
    color='Grade', 
    size='Attendance (%)',  # Bubble size based on Attendance
    hover_data=['Department', 'Sleep_Hours_per_Night'],  # Extra details on hover
    title='Study Hours vs. Final Score (Colored by Grade)',
    labels={
        'Study_Hours_per_Week': 'Study Hours per Week',
        'Final_Score': 'Final Score'
    },
    template='plotly_dark'
)

# Customize layout
fig.update_layout(
    xaxis_title='Study Hours per Week',
    yaxis_title='Final Score',
    legend_title='Grade'
)

# Show the plot
fig.show()

import pandas as pd
import plotly.express as px

# Load the dataset (replace with your actual file path if needed)
file_path = 'your_dataset.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Create the bubble chart
fig = px.scatter(
    df, 
    x='Study_Hours_per_Week', 
    y='Final_Score', 
    size='Attendance (%)',  # Bubble size based on Attendance
    color='Department',  # Color by Department
    hover_data=['Grade', 'Sleep_Hours_per_Night'],  # Extra info on hover
    title='Study Hours vs. Final Score (Bubble Size = Attendance)',
    labels={
        'Study_Hours_per_Week': 'Study Hours per Week',
        'Final_Score': 'Final Score'
    },
    template='plotly_dark'
)

# Customize layout
fig.update_layout(
    xaxis_title='Study Hours per Week',
    yaxis_title='Final Score',
    legend_title='Department'
)

# Show the plot
fig.show()




# Load the dataset (replace with your actual file path if needed)
file_path = 'cleaned.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Create the bubble chart
fig = px.scatter(
    df, 
    x='Study_Hours_per_Week', 
    y='Final_Score', 
    size='Attendance (%)',  # Bubble size based on Attendance
    color='Department',  # Color by Department
    hover_data=['Grade', 'Sleep_Hours_per_Night'],  # Extra info on hover
    title='Study Hours vs. Final Score (Bubble Size = Attendance)',
    labels={
        'Study_Hours_per_Week': 'Study Hours per Week',
        'Final_Score': 'Final Score'
    },
    template='plotly_dark'
)

# Customize layout
fig.update_layout(
    xaxis_title='Study Hours per Week',
    yaxis_title='Final Score',
    legend_title='Department'
)

# Show the plot
fig.show()



