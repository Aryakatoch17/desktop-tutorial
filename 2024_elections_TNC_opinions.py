import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for generating fake data
fake = Faker()

# Function to generate random public opinion
def generate_opinion():
    opinions = ["Supportive", "Neutral", "Opposing"]
    return random.choice(opinions)

# Generate fake data for the CSV file
data = []
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

while start_date <= end_date:
    timestamp = start_date.strftime("%Y-%m-%d %H:%M:%S")
    username = fake.user_name()
    opinion = generate_opinion()

    data.append({
        "Timestamp": timestamp,
        "Username": username,
        "Opinion": opinion
    })

    start_date += timedelta(minutes=random.randint(5, 60))

# Define CSV file headers
headers = ["Timestamp", "Username", "Opinion"]

# Write data to CSV file
csv_file_path = "2024_elections_TNC_opinions.csv"
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    # Write headers
    writer.writeheader()

    # Write data rows
    writer.writerows(data)

print(f"Fake CSV file '{csv_file_path}' created successfully.")