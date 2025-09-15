import time
from datetime import date

today = date(2025, 9, 15)
print(f"today: {today}")
print(f"year: {today.year}")
print(f"month: {today.month}")
print(f"day: {today.day}")

# creating date object from timestamp
timestamp = time.time()
now = date.fromtimestamp(timestamp)
print(now)
