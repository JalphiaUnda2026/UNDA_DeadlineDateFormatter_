# Version 2: Added Date Formatting !!
from datetime import datetime

title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Date time ouuu
event_date = datetime(year, month, day)

# Format the outputs
formatted_title = title.upper()
month_name = event_date.strftime("%B")      
weekday_name = event_date.strftime("%A")    
readable_date = f"{month_name} {day}, {year}"

# final output
print("\nFormatted Output:")
print(f"Event: {formatted_title}")
print(f"Date: {readable_date}")
print(f"Year: {year}")
print(f"Month: {month_name}")
print(f"Day: {day}")
print(f"Weekday: {weekday_name}")
