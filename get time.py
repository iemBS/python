import console 
import time
import datetime
import pytz
from tzwhere import tzwhere

startTmStr = input("start time (YYYY-MM-DDTHH:MM):")
#endTm = input("end time (YYYY-MM-DDTHH:MM):")

startTm2 = datetime.datetime.strptime(startTmStr,"%Y-%m-%dT%H:%M")

yymmddTmStr = startTm2.strftime("%y%m%d")
print("start time in YYMMDD format: " + yymmddTmStr)

mongoDbTmStr = 'ISODate("' + startTmStr + ':00Z")'
print("start time in Mongo DB ISO format: " + mongoDbTmStr)

print("start time offset from GMT based on lat & long: xxx: need to do")

offsetFromGMT = 0 # hrs between dance location and greenwuch, UK

#tzwhere = tzwhere.tzwhere()


#time.strptime("30 Nov 00", "%d %b %y")  

#tmField = 'ISODate("2017-02-08T05:00:00Z")'
