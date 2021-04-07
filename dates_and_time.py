from datetime import datetime, timezone, timedelta

date = datetime.now()
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1, )

print(date)  # 2021-04-07 10:18:36.575811
print(today)  # 2021-04-07 14:18:36.575818+00:00
print(tomorrow)  # 2021-04-08 14:18:36.575818+00:00

print(today.strftime('%d-%m-%Y %H:%M:%S'))  # 07-04-2021 14:18:28


user_date = input('Enter the date in YYYY-mm-dd format: ')  # 1990-10-04
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)  # 1990-10-04 00:00:00  - hours,min and sec default to 0



