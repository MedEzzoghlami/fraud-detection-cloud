import pandas as pd
import random
from datetime import datetime, timedelta

# Number of fake transactions
num_transactions = 100

# Users
users = ['user1', 'user2', 'user3', 'user4', 'user5']

# Locations
locations = ['tunis', 'gafsa', 'sfax', 'biert', 'gabes']

# Generate random transactions
data = []
start_time = datetime.now()

for i in range(1, num_transactions + 1):
    transaction = {
        'transaction_id': i,
        'user_id': random.choice(users),
        'amount': round(random.uniform(10, 5000), 2),  # amount between $10 and $5000
        'location': random.choice(locations),
        'timestamp': (start_time + timedelta(minutes=i*5)).strftime('%Y-%m-%d %H:%M:%S'),
        'fraud': random.choices([0, 1], weights=[90, 10])[0]  # 10% fraud
    }
    data.append(transaction)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV in data/ folder
df.to_csv('../data/transactions.csv', index=False)

print("Fake dataset generated: ../data/transactions.csv")
