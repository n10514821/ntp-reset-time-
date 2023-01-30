import ntplib
from time import *
from datetime import datetime
import win32api
import ctypes, sys


#This code resets the time on your computer by connecting to the Australian NTP
#server. To run this cody you need to download python modules ntplib and pywin32
#Links
#https://pypi.org/project/ntplib/
#https://pypi.org/project/pywin32/
#Run as a administrator to get script to function or un # ctypes


#Note if issues occur reset time with windows then run program

c = ntplib.NTPClient()
# Provide the respective ntp server ip in below function
response = c.request('au.pool.ntp.org', version=3)
response.offset

date = datetime.fromtimestamp(response.orig_time)



year = date.year
month = date.month
dayOfWeek = date.weekday()
day =   date.day
hour =  date.hour -10
minute =date.minute
second =date.second
millseconds =round(date.microsecond/1000)
print("year is ",year )
print("month is ",month)
print("dayOfWeek is ",dayOfWeek)
print("hour is ",hour)
print("minute is ",minute)
print("second is ",second)
print("millseconds is ",millseconds)
#ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

win32api.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds)


