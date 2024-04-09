import json
import csv

# Define the file paths
json_file_path = r'Data/data.json'
csv_file_path = r'Data/output.csv'

# Load JSON data from file
try:
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print(f"Error: JSON file '{json_file_path}' not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: JSON file '{json_file_path}' contains invalid JSON data.")
    exit(1)

# Extract headers from the first question
headers = data['questions'][0].keys()

# Write data to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    
    # Write headers
    writer.writeheader()
    
    # Write each question as a row in CSV
    for question in data['questions']:
        writer.writerow(question)

print(f"CSV file successfully created at '{csv_file_path}'.")
