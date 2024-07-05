import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Define a list of custom email domains
custom_domains = ['company1.com', 'company2.net', 'company3.org', 'customdomain.com']

# Generate mock data
mock_data = []
for _ in range(10):
    domain = fake.random_element(custom_domains)
    mock_data.append({
        'id': fake.unique.random_int(min=100000, max=999999),
        'email': fake.ascii_email(),
        'firstName': fake.first_name(),
        'lastName': fake.last_name() 
    })

# Convert mock data to a DataFrame
df = pd.DataFrame(mock_data, columns=['id', 'email', 'firstName', 'lastName', 'areaCode'])

# Save to CSV
df.to_csv('mock_data_table.csv', index=False)
print("Mock data saved to mock_data.csv")
