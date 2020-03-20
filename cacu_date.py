



import time
import datetime
datetime.timedelta
#2018.9.22 15:36
start_time = datetime.datetime(2018, 9, 22, 15, 36)
end_time = datetime.datetime.now()
time_passed = end_time - start_time

days_passed = time_passed.days + time_passed.seconds / 60 / 60 / 24
hours_passed = time_passed.days * 24 + time_passed.seconds / 3600
minutes_passed = time_passed.days * 24 * 60 + time_passed.seconds / 60
seconds_passed = time_passed.days * 24 * 60 * 60 + time_passed.seconds
print(u"相识 %s 天" % str(days_passed))
print(u"相识 %s 小时" % str(hours_passed))
print(u"相识 %s 分钟" % str(minutes_passed))
print(u"相识 %s 秒" % str(seconds_passed))