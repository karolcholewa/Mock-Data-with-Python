import json
from faker import Faker

# Initialize the Faker instance
fake = Faker()

# Define a list of custom email domains
custom_domains = ['company1.com', 'company2.net', 'company3.org', 'customdomain.com']

# Generate mock data for 10 items
mock_data = []
for _ in range(10000):
    domain = fake.random_element(custom_domains)
    item = {
        'id': fake.unique.random_int(min=100000, max=999999),
       'email': f"{fake.user_name()}@{domain}",
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
    }
    mock_data.append(item)

# Save to a text file (e.g., "mock_data.txt")
with open("mock_data_json.txt", "w") as file:
    json.dump(mock_data, file, indent=4)

print("Mock data saved to mock_data.txt")
