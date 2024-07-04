import pandas as pd
import csv

# Generate mock data (you can customize this as needed)
mock_data = []
for i in range(1, 101):
    mock_data.append({
        '#id': i,
        '#email': f'user{i}@example.com'
    })

# Convert mock data to a DataFrame
df = pd.DataFrame(mock_data, columns=['#id', '#email'])

# Save the DataFrame to a CSV file
df.to_csv('sampleData.csv', index=False)
