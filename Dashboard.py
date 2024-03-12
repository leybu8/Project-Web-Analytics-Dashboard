import pandas as pd
import plotly.express as px

# Load the web analytics data into a Pandas DataFrame
analytics = pd.read_csv('web_analytics.csv', parse_dates=['timestamp'])

# Drop any rows with missing values
analytics.dropna(inplace=True)

# Convert duration from seconds to minutes
analytics['duration'] = analytics['duration'] / 60

# Extract additional features from the data
analytics['day'] = analytics['timestamp'].dt.day
analytics['month'] = analytics['timestamp'].dt.month
analytics['year'] = analytics['timestamp'].dt.year
analytics['hour'] = analytics['timestamp'].dt.hour

# Calculate the total number of visits and unique users
total_visits = len(analytics)
unique_users = analytics['user_id'].nunique()

# Calculate average duration per page
avg_duration = analytics.groupby('page')['duration'].mean().reset_index()

# Visualize the data using Plotly
fig = px.scatter(analytics, x='timestamp', y='duration', color='device', hover_data=['page', 'referrer'])
fig.update_layout(title='Page Visit Duration by Device')
fig.show()

print(f"Total Visits: {total_visits}")
print(f"Unique Users: {unique_users}")
print(f"Average Page Visit Duration (minutes):\n{avg_duration}")