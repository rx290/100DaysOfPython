"""Write a Python program to parse a string representing time and returns the structure time. 
Sample Output:
String representing time: 22 January, 2020
time.struct_time(tm_year=2020, tm_mon=1, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=22, tm_isdst=-1)
String representing time: 30 Nov 00
time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
String representing time: 04/11/15 11:55:23
time.struct_time(tm_year=2015, tm_mon=4, tm_mday=11, tm_hour=11, tm_min=55, tm_sec=23, tm_wday=5, tm_yday=101, tm_isdst=-1)
String representing time: 12-11-2019
time.struct_time(tm_year=2019, tm_mon=12, tm_mday=11, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=345, tm_isdst=-1)
String representing time: 13::55::26
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=13, tm_min=55, tm_sec=26, tm_wday=0, tm_yday=1, tm_isdst=-1) """ 
