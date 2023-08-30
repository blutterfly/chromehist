# chromehist
Chrome History processing 

Downloading your Chrome history isn't a built-in feature of Google Chrome, but there are a few workarounds that can help you achieve this:

## Method 1: Google Takeout
Go to Google Takeout: Open your browser and go to Google Takeout.
Sign in: Log in to the Google account you use with Chrome.
Deselect All: By default, all data types are selected for download. Click "Deselect All."
Select Chrome: Scroll down and select just "Chrome."
Choose Data Types: Click on "All Chrome data included" to choose specifically what Chrome data you want. Make sure to select "Browsing History."
Create Export: Scroll down and click "Next" and then "Create export."
Download: Once the export is created, you'll get a link to download it. This will be a .zip file containing your history in JSON format.

## Method 2: Manual Method for Windows Users
Locate Chrome History File: Your Chrome history file is usually located in C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\. The history is stored in a file named History (with no file extension).
Copy the File: To make sure you don't corrupt your current history, copy this file to another location.
View with SQLite Browser: The history file is an SQLite database, so you can use an SQLite browser to view and export the data.

## Method 3: Using a Script
As you're a Python software developer, you may find it convenient to write a Python script to extract the history data from the SQLite database. You can use the sqlite3 library to query the database and then write the results to a CSV or JSON file.

Here's a very basic example that queries URLs and their last visit time:
