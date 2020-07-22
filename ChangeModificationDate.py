# coding=utf-8
import os
import time
import datetime

fileLocation = r"1024.gif"
year = 2018
month = 1
day = 2
hour = 18
minute = 0
second = 56

date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())

os.utime(fileLocation, (modTime, modTime))