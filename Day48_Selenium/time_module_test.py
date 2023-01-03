import time

# Date 1
date1 = "1 Jan 2000 00:00:00"

# Date2
date2 = "22 Aug 2019 00:00:00"

# Parse the date strings
# and convert it in
# time.struct_time object using
# time.strptime() method

# Get the time in seconds
# since the epoch
# for both time.struct_time objects
time1 = time.mktime(12987343)
print(time1)
