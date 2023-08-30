import sqlite3
import csv
import re
from datetime import datetime, timedelta


# Function to convert WebKit time to datetime
def webkit_to_datetime(webkit_timestamp):
    epoch_start = datetime(1601, 1, 1)
    delta = timedelta(microseconds=webkit_timestamp)
    return epoch_start + delta


# Function to convert datetime to WebKit time
def datetime_to_webkit(py_datetime):
    epoch_start = datetime(1601, 1, 1)
    delta = py_datetime - epoch_start
    return int(delta.total_seconds() * 1000000)


# Define date range in Python datetime format
start_date = datetime(2023, 8, 25)
end_date = datetime(2023, 8, 29)

# Convert to WebKit timestamp format
start_timestamp = datetime_to_webkit(start_date)
end_timestamp = datetime_to_webkit(end_date)

# Connect to SQLite database
conn = sqlite3.connect("History")
cursor = conn.cursor()

# Define regular expression pattern for URL filtering
pattern = re.compile(r'-[a-f1-9]{12}')

# Query the urls and last_visit_time columns with a date filter
query = f"SELECT url, last_visit_time FROM urls WHERE last_visit_time >= {start_timestamp} AND last_visit_time <= {end_timestamp}"
cursor.execute(query)

# Write the results to a CSV file
with open('filtered_chrome_history.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Last Visit Time'])

    for row in cursor.fetchall():
        url = row[0]
        last_visit_time = webkit_to_datetime(row[1])

        # Use re.search() to filter URLs based on the pattern
        if re.search(pattern, url):
            writer.writerow([url, last_visit_time])
