from datetime import datetime, timedelta

#ex1
# current_date = datetime.now()

# result_date = current_date - timedelta(days=5)

# print("Current Date:", current_date.strftime("%Y-%m-%d"))
# print("Date five days ago:", result_date.strftime("%Y-%m-%d"))

#ex2
# today = datetime.now()
# yesterday = today - timedelta(days = 1)
# tomorrow = today + timedelta(days = 1)

# print(today)
# print(yesterday)
# print(tomorrow)

#ex3
# today = datetime.now()
# print(today.strftime("%d-%m-%Y"))

#ex4
from datetime import datetime

date_1 = '24/7/2021 11:13:08'
date_2 = '24/7/2021 11:23:18'

date_format_str = '%d/%m/%Y %H:%M:%S'

start = datetime.strptime(date_1, date_format_str)
end =   datetime.strptime(date_2, date_format_str)

diff = end - start

print(diff.total_seconds())