import sqlite3
import csv
from datetime import datetime, timedelta

# Replace this with the path to your own History file
history_db_path = "History"

# Function to convert WebKit time to datetime
def webkit_to_datetime(webkit_timestamp):
    epoch_start = datetime(1601, 1, 1)
    delta = timedelta(microseconds=webkit_timestamp)
    return epoch_start + delta

# Connect to the SQLite database
conn = sqlite3.connect(history_db_path)
cursor = conn.cursor()

# Query the urls and last_visit_time columns from the urls table
cursor.execute("SELECT url, last_visit_time FROM urls")

# Write the results to a CSV file
with open('chrome_history.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Last Visit Time'])
    for row in cursor.fetchall():
        url = row[0]
        last_visit_time = webkit_to_datetime(row[1])
        writer.writerow([url, last_visit_time])