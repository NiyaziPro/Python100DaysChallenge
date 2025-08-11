import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_weak = now.weekday()
print(day_of_weak)

date_of_birth = dt.datetime(year=1990, month=1, day=1, hour=9)
print(date_of_birth)
