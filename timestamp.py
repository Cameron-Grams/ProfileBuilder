
from datetime import datetime
ts = int(1634506965277/1000)
#  
utc_time_obj = datetime.utcfromtimestamp(ts)

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

print(utc_time_obj)
print(utc_time_obj.strftime('%Y-%m-%d %H:%M:%S'))
