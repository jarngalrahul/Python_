import datetime as dt

now = dt.datetime.now()
print(now)  # output: 2022-12-20 11:49:56.650621
print(type(now))  # output: <class 'datetime.datetime'> datetime object
print(now.year)  # output: 2022
print(type(now.year))  # output: <class 'int'>
day_of_week = now.weekday()
print(day_of_week)  # output: 1(Tuesday)

day_of_birth = dt.datetime(year=1998, month=3, day=30)
print(day_of_birth)
